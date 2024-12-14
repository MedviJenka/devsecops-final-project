import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    AI_SERVER_PRIVATE_ADDRESS = os.getenv('AI_SERVER_PRIVATE_ADDRESS')
    APP_SERVER_PRIVATE_ADDRESS = os.getenv('APP_SERVER_PRIVATE_ADDRESS')
    AI_PORT = os.getenv('AI_PORT')
    APP_PORT = os.getenv('APP_PORT')
    HOST = os.getenv('HOST')
    DEBUG = True
