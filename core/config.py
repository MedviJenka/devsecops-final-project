import os
from enum import StrEnum
from dotenv import load_dotenv


load_dotenv()


class ConfigEnvironment(StrEnum):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')


