# CPU #
## CPU Usage Overall in a Cluster that is greater than a defined threshold ##

A measurement of the total CPU Cores used expressed as a percentage in a cluster vs alloctable cores. The alert will check if it is greater than 90% utilization via PromQL.

**PromQL Query**:

```
((sum by (kube_cluster_name) (sysdig_container_cpu_cores_used) / sum by (kube_cluster_name)(kube_node_status_allocatable_cpu_cores)) * 100) > 90
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_cluster_name }} CPU Utilization is high`

## CPU Usage Overall on a Node that is greater than a defined threshold

A measurement of the total CPU Cores used on a Node expressed as a percentage against the allocatable CPU Cores. The alert will check if it is greater than 90% utilization via PromQL

**PromQL Query**:

```
((sum by (kube_node_name, kube_cluster_name) (sysdig_container_cpu_cores_used) / on (kube_node_name) group_left sum by (kube_node_name)(kube_node_status_allocatable_cpu_cores)) * 100) > 90
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_node_name }} CPU Utilization is high in {{ kube_cluster_name }}`

## CPU Usage of a Namespace compared against the Cluster alloctable CPU Cores is greater than a defined threshold

A measurement of the total CPU Cores used by a namespace compared to the alloctable Cores in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_namespace_name) (sysdig_container_cpu_cores_used) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_cpu_cores)) * 100) > 25
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_namespace_name }} CPU Utilization is high in {{ kube_cluster_name }}`


## CPU Usage of a of a workload against the Cluster total CPU Cores is greater than defined threshold ##

A measurement of the total CPU Cores used by a workload compared to the total Cores in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_workload_name, kube_namespace_name) (sysdig_container_cpu_cores_used) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_cpu_cores)) * 100) > 10
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_workload_name }} CPU Utilization is high in {{ kube_cluster_name }}`

## CPU Usage of a of a container against the Cluster total CPU Cores is greater than defined threshold ##

A measurement of the total CPU Cores by percent used by a container compared to the total Cores in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_workload_name, kube_namespace_name, container_name) (sysdig_container_cpu_cores_used) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_cpu_cores)) * 100) > 10
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ container_name }} in {{ kube_namespace_name }}/{{ kube_workload_name }} CPU Utilization is high in {{ kube_cluster_name }}`


# Memory #
## Memory Usage Overall in a Cluster that is greater than a defined threshold ##

A measurement of the total Memory Bytes used expressed as a percentage. The alert will check if it is greater than 90% utilization via PromQL.

**PromQL Query**:

```
(sum by (kube_cluster_name) (sysdig_container_memory_used_bytes) / sum by (kube_cluster_name)(kube_node_status_capacity_memory_bytes) * 100) > 90
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_cluster_name }} Memory Utilization is high`

## Memory Usage Overall on a Node that is greater than a defined threshold

A measurement of the total CPU Cores used on a Node expressed as a percentage. The alert will check if it is greater than 90% utilization via PromQL

**PromQL Query**:

```
(sum by (kube_node_name, kube_cluster_name) (sysdig_container_memory_used_bytes) / on (kube_node_name) group_left sum by (kube_node_name)(kube_node_status_allocatable_memory_bytes) * 100) * 100
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_node_name }} CPU Utilization is high on {{ kube_cluster_name }}`

## Memory Usage of a Namespace compared against the Cluster alloctable Memory is greater than a defined threshold

A measurement of the total Memory Bytes used by a namespace compared to the total Cores in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_namespace_name) (sysdig_container_memory_used_bytes) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_memory_bytes)) * 100) > 25
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_namespace_name }} Memory Utilization is high in {{ kube_cluster_name }}`


## Memory Usage of a of a workload against the Cluster alloctable Memory is greater than defined threshold ##

A measurement of the total Memory used by a workload compared to the alloctable Memory in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_workload_name, kube_namespace_name) (sysdig_container_memory_used_bytes) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_memory_bytes)) * 100) > 10
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ kube_workload_name }}/{{ kube_namespace_name }} Memory Utilization is high in {{ kube_cluster_name }}`

## Memory Usage of a of a container against the Cluster alloctable Memroy is greater than defined threshold ##

A measurement of the total Memory by percent used by a container compared to the alloctable Memory in the cluster

**PromQL Query**
```
((sum by (kube_cluster_name, kube_namespace_name, kube_workload_name, container_name) (sysdig_container_memory_used_bytes) / on (kube_cluster_name) group_left sum by (kube_cluster_name)(kube_node_status_allocatable_memory_bytes)) * 100) > 10
```

**Duration**: 10 Min

**Notification Subject & Title Event**

`{{ container_name }} in {{ kube_namespace_name }}/{{ kube_workload_name }} Memory Utilization is high in {{ kube_cluster_name }}`