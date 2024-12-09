from openai import OpenAI
from core.config import Config
from dataclasses import dataclass


@dataclass
class RoastAgent:

    client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def roast_me(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a sarcastic AI who roasts the user and tells DevOps jokes. Be mean and funny!"},
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o",
            temperature=0.5
        )
        content = response.choices[0].message.content
        return content
