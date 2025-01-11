import requests
from app.core.config import PortConfig, PrivateIPConfig


class RequestManager:

    def __init__(self) -> None:
        self.url = f"http://{PrivateIPConfig.BACKEND_IP}:{PortConfig.BACKEND_PORT}/roast"

    def request_handler(self, input_text: str):
        headers = {"Content-Type": "application/json"}
        payload = {"input": input_text}

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def send_request(self, user_input: str) -> str:
        response = self.request_handler(user_input)
        if "roast" in response:
            return response["roast"].strip()
        elif "error" in response:
            return f"Error: {response['error']}"
        else:
            return "Unexpected response format"

    def health_check(self) -> int:
        try:
            response = requests.get(self.url)
            return response.status_code
        except requests.exceptions.RequestException as e:
            raise Exception(f"Health check failed: {str(e)}")
