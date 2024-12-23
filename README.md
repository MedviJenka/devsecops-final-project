# minikube windows installation 

documentation:
* https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download

`
New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -inotcontains 'C:\minikube'){
  [Environment]::SetEnvironmentVariable('Path', $('{0};C:\minikube' -f $oldPath), [EnvironmentVariableTarget]::Machine)
}

`


# CI/CD Pipeline with SonarQube Integration

This document outlines the steps to configure a CI/CD pipeline in Jenkins with SonarQube integration for code analysis and quality gate checks. The pipeline automates the process of building, analyzing, and deploying your application.

---

## Prerequisites

Before you begin, ensure the following tools are installed and configured:

- **Jenkins** (with required plugins installed)
- **SonarQube** server
- **Git** repository for your project
- **Node.js** and **JDK** installed and configured in Jenkins
- **SonarQube Scanner** installed in Jenkins via **Global Tool Configuration**

---

## Setup Instructions

### 1. Create the SonarQube Token

1. Log in to your **SonarQube** server.
2. Navigate to **My Account** → **Security** → **Generate Tokens**.
3. Copy the token for later use.

---

### 2. Add the Token to Jenkins

1. Go to **Jenkins Dashboard** → **Manage Jenkins** → **Credentials**.
2. Add a new **Secret Text** credential:
   - **ID**: `SONAR_TOKEN`
   - **Secret**: Paste the SonarQube token.

---

### 3. Configure SonarQube in Jenkins

1. Navigate to **Manage Jenkins** → **Configure System**.
2. Under **SonarQube Servers**:
   - Add a new SonarQube server.
   - Provide a name (e.g., `sonar-server`) and the server URL.
   - Add the token credential by selecting it from the drop-down menu.
3. Click **Save**.

---

### 4. Install SonarQube Scanner in Jenkins

1. Go to **Manage Jenkins** → **Global Tool Configuration**.
2. Under **SonarQube Scanner**, add a new scanner:
   - Provide a name (e.g., `sonar-scanner`).
   - Allow Jenkins to install the scanner automatically.

---

### 5. Create a Webhook for Jenkins in GitHub

1. In your GitHub repository:
   - Navigate to **Settings** → **Webhooks** → **Add webhook**.
2. Configure the webhook:
   - **Payload URL**: `<Jenkins_URL>/github-webhook/`
   - **Content type**: `application/json`
   - Select **Just the push event**.
3. Click **Add webhook**.

---

## Pipeline Script

The following Jenkins pipeline script defines a CI/CD pipeline with SonarQube integration:

```groovy
pipeline {

    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                git branch: 'main', url: 'https://github.com/MedviJenka/roast-bot.git'
            }
        }

        stage("Sonarqube Analysis") {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''$SCANNER_HOME/bin/sonar-scanner
                        -Dsonar.projectName=app
                        -Dsonar.projectKey=app
                        -Dsonar.host.url=http://192.168.1.104:91
                    '''
                }
            }
        }

        stage("quality gate") {
            steps {
                script {
                    waitForQualityGate abortPipeline: false, credentialsId: 'SONAR_TOKEN'
                }
            }
        }
    }
}



