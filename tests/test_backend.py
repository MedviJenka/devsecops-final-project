import requests


BE_URL = "http://localhost:88"
FE_URL = "http://localhost:89"


class TestContainers:

    def test_backend_health(self) -> None:
        response = requests.get(BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'server is up' in response.text

    def test_api_key_success(self) -> None:
        response = requests.get(BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'api_key', 'success' in response.text

    def test_frontend_health(self) -> None:
        response = requests.get(f'{FE_URL}/health')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert "Service is healthy" in response.text
