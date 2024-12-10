pipeline {
  agent none
  environment {
    AI_PORT = "${env.AI_PORT}"
    APP_PORT = "${env.APP_PORT}"
    HOST = "${env.HOST}"
    OPENAI_API_KEY = "${env.OPENAI_API_KEY}"
  }

   stages {
    stage('Build Tests Image') {
      agent {
        docker {
          image 'docker:latest'
          args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
      }
      steps {
        script {
          // Build the tests image from the provided Dockerfile
          sh 'docker-compose build'
          sh 'docker-compose up -d'
        }
      }
    }

    stage('Run Tests') {
      agent {
        docker {
          image "${TEST_IMAGE}"
        }
      }
      steps {
        script {
          // Run the tests within the built Docker image
          sh 'pytest /tests/tests/test_requests.py'
        }
      }
    }
  }

}
