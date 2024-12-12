pipeline {

    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'compose.yaml'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                git branch: 'main', url: 'https://github.com/MedviJenka/roast-bot.git'
            }
        }

        stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarScanner';
            withSonarQubeEnv() {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }


//         stage('Build Docker Image') {
//             steps {
//                 echo 'Building the Docker image...'
//                 script {
//                     sh """
//                     ${DOCKER_COMPOSE_FILE} up --d --build
//                     """
//                 }
//             }
//         }


    }
}
