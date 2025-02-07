from dataclasses import dataclass
from kubernetes import client, config


@dataclass
class K8SClusterManager:

    namespace: str = "default"

    def __post_init__(self) -> None:
        # Load Kubernetes configuration
        try:
            config.load_kube_config()
        except config.config_exception.ConfigException:
            config.load_incluster_config()

        # Initialize Kubernetes clients
        self.core_v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()

    def get_logs(self, pod_name: str) -> list:
        """Retrieves logs for a specified pod in the given namespace."""
        if not pod_name:
            raise ValueError("Pod name must be provided")

        try:
            logs = self.core_v1.read_namespaced_pod_log(
                name=pod_name,
                namespace=self.namespace,
                pretty=True
            )
            return logs.splitlines()
        except client.exceptions.ApiException as e:
            raise RuntimeError(f"Error retrieving logs: {e}")

    def list_pods(self) -> list:
        """Lists all pods in the specified namespace."""
        try:
            pods = self.core_v1.list_namespaced_pod(namespace=self.namespace)
            return [
                {
                    "name": pod.metadata.name,
                    "uid": pod.metadata.uid,
                    "phase": pod.status.phase,
                    "conditions": [
                        {"type": c.type, "status": c.status}
                        for c in (pod.status.conditions or [])
                    ]
                }
                for pod in pods.items
            ]
        except Exception as e:
            raise RuntimeError(f"Error listing pods: {e}")

    def list_nodes(self) -> list:
        """Lists all nodes in the cluster."""
        try:
            nodes = self.core_v1.list_node()
            return [
                {
                    "name": node.metadata.name,
                    "conditions": [
                        {"type": c.type, "status": c.status}
                        for c in node.status.conditions
                    ],
                    "capacity": {
                        "cpu": node.status.capacity.get("cpu", "N/A"),
                        "memory": node.status.capacity.get("memory", "N/A"),
                    },
                    "phase": getattr(node.status, "phase", "Unknown"),
                }
                for node in nodes.items
            ]
        except Exception as e:
            raise RuntimeError(f"Error listing nodes: {e}")

    def list_deployments(self) -> list:
        """Lists all deployments in the specified namespace."""
        try:
            deployments = self.apps_v1.list_namespaced_deployment(namespace=self.namespace)
            return [
                {
                    "name": dep.metadata.name,
                    "replicas": dep.spec.replicas,
                    "availableReplicas": dep.status.available_replicas or 0,
                    "readyReplicas": dep.status.ready_replicas or 0,
                }
                for dep in deployments.items
            ]
        except Exception as e:
            raise RuntimeError(f"Error listing deployments: {e}")
