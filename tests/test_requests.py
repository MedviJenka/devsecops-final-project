import requests
from app.request_manager import RequestManager
from core.config import PortConfig, PrivateIPConfig

request = RequestManager()


class TestContainers:

    """
    for local tests change private ip config to http://localhost
    """

    def test_nginx(self) -> None:
        url = f"http://{PrivateIPConfig.NGINX_PRIVATE_IP}:80"
        response = requests.get(url)
        assert response.status_code == 200

    def test_ai_server_health(self) -> None:
        url = f"http://{PrivateIPConfig.AI_SERVER_PRIVATE_IP}:{PortConfig.AI_PORT}/health"
        response = requests.get(url)
        assert response.status_code == 200

    def test_app_server_health(self) -> None:
        url = f"http://{PrivateIPConfig.APP_SERVER_PRIVATE_IP}:{PortConfig.APP_PORT}/health"
        response = requests.get(url)
        assert response.status_code == 200

    def test_gif_image(self) -> None:
        url = f"http://{PrivateIPConfig.APP_SERVER_PRIVATE_IP}:{PortConfig.APP_PORT}/static/images/roasted.gif"
        response = requests.get(url)
        assert response.status_code == 200

    def test_allure_server(self) -> None:
        url = f"http://{PrivateIPConfig.ALLURE_SERVER_PRIVATE_IP}:5050"
        response = requests.get(url)
        assert response.status_code == 200
