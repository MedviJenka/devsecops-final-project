import os
from dotenv import load_dotenv


load_dotenv()


class AppConfig:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HOST = '0.0.0.0'
    DEBUG = True


class PortConfig:
    BACKEND_PORT = 88
    FRONTEND_PORT = 89


class PrivateIPConfig:
    FRONTEND_IP = os.getenv('FRONTEND_IP')
    BACKEND_IP = os.getenv('BACKEND_IP')
