# Pods #
## Pods have entered a waiting state that is not ContainerCreating ##

Pods in a workload have entered a state of CrashloopBackoff, ImagePullError, etc.

**PromQL Query**:

```
sum by (kube_cluster_name, kube_namespace_name, kube_workload_name, kube_pod_name, reason)(kube_pod_container_status_waiting_reason{reason!="ContainerCreating"}) >= 1 
```

**Duration**: 1 Min

**Notification Subject & Title Event**

`{{ kube_pod_name }}/{{ kube_workload_name }}/in {{ kube_namespace_name }} has entered a waiting state with {{ reason }}.`

## Pods have gone into Pending Status ##
(avg(kube_workload_pods_status_phase{kube_pod_phase="Pending"}) by (kube_namespace_name, kube_workload_name))

## Workload has less pods than desired ##
((avg(kube_workload_status_running{kube_workload_name="podinfo"}) by (kube_namespace_name, kube_workload_name)) < (avg(kube_workload_status_desired{kube_workload_name="podinfo"}) by (kube_workload_name, kube_namespace_name)))

# Nodes #
## Node has entered a NotReady State ##

A node in a cluster has entered a not ready state.

**PromQL Query**:

```
kube_node_status_condition{condition="Ready",status="true"} == 0
```

**Duration**: 1 Min

**Notification Subject & Title Event**

`{{ kube_node_name }} in {{ kube_cluster_name }} has become {{ condition }}.`



