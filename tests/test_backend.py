import requests


class TestContainers:

    BE_URL = "http://127.0.0.1:88"
    FE_URL = "http://127.0.0.1:89"

    def test_backend_health(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'server is up' in response.text

    def test_api_key_success(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'api_key', 'success' in response.text

    def test_frontend_health(self) -> None:
        response = requests.get(f'{self.FE_URL}/health')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert "Service is healthy" in response.text


class TestContainers2:

    BE_URL = "http://localhost:88"
    FE_URL = "http://localhost:89"

    def test_backend_health(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'server is up' in response.text

    def test_api_key_success(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'api_key', 'success' in response.text

    def test_frontend_health(self) -> None:
        response = requests.get(f'{self.FE_URL}/health')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert "Service is healthy" in response.text


class TestContainers3:

    BE_URL = "http://backend:88"
    FE_URL = "http://backend:89"

    def test_backend_health(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'server is up' in response.text

    def test_api_key_success(self) -> None:
        response = requests.get(self.BE_URL)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert 'api_key', 'success' in response.text

    def test_frontend_health(self) -> None:
        response = requests.get(f'{self.FE_URL}/health')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert "Service is healthy" in response.text
