from dataclasses import dataclass
from textwrap import dedent
from ai.k8s.status import K8SClusterManager
from ai.security.src.crew import SecurityBase


@dataclass
class RunTestCrew(SecurityBase):

    k8s_manager = K8SClusterManager()

    def run(self) -> str:
        inputs = {'topic': dedent(f"""{self.k8s_manager.list_deployments()}""")}
        output = self.crew().kickoff(inputs=inputs)
        return output
