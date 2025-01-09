import os
from dotenv import load_dotenv


load_dotenv()


class AppConfig:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HOST = '0.0.0.0'
    DEBUG = True


class PortConfig:
    APP_PORT = 88
