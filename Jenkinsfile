pipeline {

    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml' // Path to your Docker Compose file
        IMAGE_NAME = 'roast-bot' // Replace with your app's Docker image name
        DOCKER_REGISTRY = 'your-docker-registry' // Replace with your Docker registry if applicable
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker image...'
                script {
                    sh """
                    docker-compose -f ${DOCKER_COMPOSE_FILE} build
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests inside the Docker containers...'
                script {
                    sh """
                    docker-compose -f ${DOCKER_COMPOSE_FILE} up -d
                    docker exec roast-bot-app pytest tests/ # Replace with your test command
                    docker-compose -f ${DOCKER_COMPOSE_FILE} down
                    """
                }
            }
        }

        stage('Push Docker Image') {
            when {
                branch 'main' // Only push the image on the main branch
            }
            steps {
                echo 'Pushing the Docker image to the registry...'
                script {
                    sh """
                    docker tag ${IMAGE_NAME} ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest
                    docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main' // Only deploy from the main branch
            }
            steps {
                echo 'Deploying the application...'
                script {
                    sh """
                    docker-compose -f ${DOCKER_COMPOSE_FILE} pull
                    docker-compose -f ${DOCKER_COMPOSE_FILE} up -d
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
            script {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans'
            }
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
