from openai import OpenAI
from dataclasses import dataclass
from core.config import ConfigEnvironment


@dataclass
class RoastAgent:

    client = OpenAI(api_key=ConfigEnvironment.OPENAI_API_KEY)

    def roast_me(self, user_input: str) -> str:
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a sarcastic AI who roasts the user and tells DevOps jokes"
                                              "be mean and funny!"},
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o",
            temperature=0.5
        )

        content = response.choices[0].message.content
        return content
