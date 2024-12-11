pipeline {

    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'compose.yml' // Path to your Docker Compose file
        IMAGE_NAME = 'roast-bot'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                git branch: 'main', url: 'https://github.com/MedviJenka/roast-bot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                script {
                    sh """
                    docker-compose up --d --build
                    """
                }
            }
        }
    }
}
