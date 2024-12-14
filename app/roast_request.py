import requests
from dotenv import load_dotenv
from core.config import Config


load_dotenv()


class RoastRequest:

    def __init__(self) -> None:
        self.url = f"{Config.AI_SERVER_PRIVATE_ADDRESS}:{Config.AI_PORT}/roast"

    def request_handler(self, input_text: str):
        headers = {"Content-Type": "application/json"}
        payload = {"input": input_text}

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def send_roast_request(self, user_input: str) -> str:
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
