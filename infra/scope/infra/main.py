from infra.scope.infra.agent import ContainerAgent
from infra.scope.infra.logs import generate_container_logs


if __name__ == '__main__':
    generate_container_logs()
    container_agent = ContainerAgent()
    container_agent.execute()
