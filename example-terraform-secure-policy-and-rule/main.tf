terraform {
  required_providers {
    sysdig = {
      source = "sysdiglabs/sysdig"
      version = "0.5.28"
    }
  }
}

provider "sysdig" {
  # Configuration options
    sysdig_secure_url = "YOUR_SYSDIG_SECURE_URL"
    #sysdig_monitor_api_token - (Optional) The Sysdig Monitor API token, it must be present, but you can get it from the SYSDIG_MONITOR_API_TOKEN environment variable. 
    #Required if any sysdig_monitor_* resource or data source is used.

    #sysdig_secure_api_token - (Optional) The Sysdig Secure API token, it must be present, but you can get it from the SYSDIG_SECURE_API_TOKEN environment variable. 
    #Required if any sysdig_secure_* resource or data source is used.
}

resource "sysdig_secure_rule_falco" "ts_exclude_rancher_shell" {
  name        = "Terminal shell in container - Exclude Rancher" // ID
  description = "A shell was used as the entrypoint/exec point into a container with an attached terminal. Excluding Rancher Call"
  tags        = ["container", "shell", "mitre_execution"]

  condition = "spawned_process and container and shell_procs and proc.tty != 0 and container_entrypoint"
  output    = "A shell was spawned in a container with an attached terminal (user=%user.name %container.info shell=%proc.name parent=%proc.pname cmdline=%proc.cmdline terminal=%proc.tty container_id=%container.id image=%container.image.repository)"
  priority  = "notice"
  source    = "syscall" // syscall or k8s_audit
  append = false

  exceptions {
    name   = "rancher_shell"
    fields = ["proc.cmdline", "proc.name"]
    comps  = ["startswith", "startswith"]
    values = jsonencode([
      ["sh -c TERM=xterm-256color; export TERM; [ -x /bin/bash ] && ([ -x /usr/bin/script ] && /usr/bin/script -q -c", "sh"]
    ]) # If only one element is provided, do not specify it a list of lists.
  }
}


resource  "sysdig_secure_policy" "disallowed_container_activity" {

  name = "Disallowed Container Activities"
  description = "Container activities that are not allowed: e.g. unwanted exec's into a container outside of Rancher UI"
  severity = 4
  enabled = true

  // Scope selection
  scope = "container.id != \"\""

  // Rule selection
  rule_names = [sysdig_secure_rule_falco.ts_exclude_rancher_shell.name]

  actions {
    container = "stop"
    capture {
      seconds_before_event = 5
      seconds_after_event = 10
    }
  }

}