from infra.scope.containers.agent import ContainerAgent
from infra.scope.containers.logs import generate_container_logs


if __name__ == '__main__':
    generate_container_logs()
    container_agent = ContainerAgent()
    container_agent.execute()
