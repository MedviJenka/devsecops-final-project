import os


class AppConfig:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HOST = '0.0.0.0'
    DEBUG = True


class PortConfig:
    AI_PORT = 88
    APP_PORT = 89
