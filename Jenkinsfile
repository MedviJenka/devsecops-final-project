pipeline {
  agent none
  environment {
    AI_PORT = "${env.AI_PORT}"
    APP_PORT = "${env.APP_PORT}"
    HOST = "${env.HOST}"
    OPENAI_API_KEY = "${env.OPENAI_API_KEY}"
    JENKINS_PORT = "${env.JENKINS_PORT}"
  }

  stages {
    stage('Build and Run Services') {
      agent {
        docker {
          image 'docker:latest'
          args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
      }
      steps {
        script {
          // Build and start services using docker-compose
          sh 'docker-compose up -d --build'
        }
      }
    }

    stage('Run Tests') {
      steps {
        script {
          // Execute tests inside the "tests" container
          sh 'docker exec tests pytest /tests/tests/test_requests.py'
        }
      }
    }

    stage('Clean Up') {
      steps {
        script {
          // Stop and remove all services
          sh 'docker-compose down'
        }
      }
    }
  }
}
