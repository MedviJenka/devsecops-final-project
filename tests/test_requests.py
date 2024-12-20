import requests
import concurrent.futures
from app.request_manager import RequestManager
from core.config import PortConfig, PrivateIPConfig

request = RequestManager()


class TestContainers:

    """
    for local tests change private ip config to http://localhost
    """

    def test_sanity(self) -> None:
        assert 1 + 1 == 2
    #
    # def test_nginx_server(self) -> None:
    #     url = f"http://{PrivateIPConfig.AI_SERVER_PRIVATE_IP}:{PortConfig.AI_PORT}"
    #     response = requests.get(url)
    #     assert response.status_code == 200
    #
    # def test_micro_load_nginx(self, workers: int = 100, amount: int = 1000) -> None:
    #
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
    #
    #         futures = [executor.submit(request.send_request, user_input='hello') for _ in range(amount)]
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             try:
    #                 response = future.result()
    #                 print(response)  # Print the result or process it
    #             except Exception as e:
    #                 print(f"Request failed: {e}")
    #
    # def test_ai_server_health(self) -> None:
    #     url = f"http://{PrivateIPConfig.AI_SERVER_PRIVATE_IP}:{PortConfig.AI_PORT}/health"
    #     response = requests.get(url)
    #     assert response.status_code == 200
    #
    # def test_app_server_health(self) -> None:
    #     url = f"http://{PrivateIPConfig.APP_SERVER_PRIVATE_IP}:{PortConfig.APP_PORT}/health"
    #     response = requests.get(url)
    #     assert response.status_code == 200
    #
    # def test_gif_image(self) -> None:
    #     url = f"http://{PrivateIPConfig.APP_SERVER_PRIVATE_IP}:{PortConfig.APP_PORT}/static/images/roasted.gif"
    #     response = requests.get(url)
    #     assert response.status_code == 200
    #
    # def test_allure_server(self) -> None:
    #     url = f"http://{PrivateIPConfig.ALLURE_SERVER_PRIVATE_IP}:5050"
    #     response = requests.get(url)
    #     assert response.status_code == 200
