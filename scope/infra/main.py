from core.container_agent.infra.agent import ContainerAgent
from core.container_agent.infra.logs import generate_container_logs


if __name__ == '__main__':
    generate_container_logs()
    container_agent = ContainerAgent()
    container_agent.execute()
