import os
from openai import OpenAI
from app.bot.prompts import PROMPT
from dataclasses import dataclass


@dataclass
class AIAgent:

    """
    send an openai request to the sever
    """

    api_key: str = os.getenv('OPENAI_API_KEY')

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
        self.client = OpenAI(api_key=self.api_key)

    def set_ai(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o",
            temperature=0.5
        )
        content = response.choices[0].message.content
        return content

    def get_ai_response(self, user_input: str) -> str:
        response = self.set_ai(user_input=user_input)
        return response
