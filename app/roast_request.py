import requests
from dotenv import load_dotenv
from core.config import Config


load_dotenv()


class RoastRequest:

    def __init__(self) -> None:
        self.url = f"http://127.0.0.1:{Config.AI_PORT}/roast"

    def request_handler(self, input_text: str):
        headers = {"Content-Type": "application/json"}
        payload = {"input": input_text}

        try:
            response = requests.post(self.url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def send_roast_request(self, user_input: str) -> str:
        """
        Sends a roast request and extracts a clean roast text.

        Args:
            user_input (str): The user's input.

        Returns:
            str: A clean roast message or an error message if the request fails.
        """
        response = self.request_handler(user_input)

        # Extract the roast if the response is valid, otherwise return the error
        if "roast" in response:
            return response["roast"].strip()  # Clean and return the roast text
        elif "error" in response:
            return f"Error: {response['error']}"
        else:
            return "Unexpected response format"
