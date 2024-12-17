import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='../.env')


class Config:
    HOST = os.getenv('HOST')
    APP_PORT = os.getenv('APP_PORT')
    DEBUG = True
