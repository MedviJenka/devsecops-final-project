import os
from dotenv import load_dotenv


load_dotenv()


class AppConfig:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HOST = os.getenv('HOST')
    DEBUG = True


class PortConfig:
    AI_PORT = os.getenv('AI_PORT')
    APP_PORT = os.getenv('APP_PORT')
    NGINX_PORT = os.getenv('NGINX_PORT')
    JENKINS_PORT = os.getenv('JENKINS_PORT')
    SONARQUBE_PORT = os.getenv('SONARQUBE_PORT')
    ALLURE_SERVER_PORT = os.getenv('ALLURE_SERVER_PORT')


class PrivateIPConfig:
    NGINX_PRIVATE_IP = os.getenv('NGINX_PRIVATE_IP')
    JENKINS_PRIVATE_IP = os.getenv('JENKINS_PRIVATE_IP')
    SONAR_DB_PRIVATE_IP = os.getenv('SONAR_DB_PRIVATE_IP')
    AI_SERVER_PRIVATE_IP = os.getenv('AI_SERVER_PRIVATE_IP')
    SONARQUBE_PRIVATE_IP = os.getenv('SONARQUBE_PRIVATE_IP')
    APP_SERVER_PRIVATE_IP = os.getenv('APP_SERVER_PRIVATE_IP')
    ALLURE_SERVER_PRIVATE_IP = os.getenv('ALLURE_SERVER_PRIVATE_IP')


class AWSElasticIP:
    AWS_ELASTIC_IP = os.getenv('AWS_ELASTIC_IP')
