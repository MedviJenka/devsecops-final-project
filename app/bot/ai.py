from openai import OpenAI
from bot.prompts import PROMPT
from core.config import AppConfig
from dataclasses import dataclass


@dataclass
class AIAgent:

    """
    send an openai request to the sever
    """

    client = OpenAI(api_key=AppConfig.OPENAI_API_KEY)

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
