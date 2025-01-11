from openai import OpenAI
from dataclasses import dataclass
from app.backend.prompts import PROMPT
from app.core.config import AppConfig


@dataclass
class Agent:

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
