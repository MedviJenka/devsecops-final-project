#!/bin/bash

sudo apt-get update

python3 --version
pip3 --version
docker --version
docker-compose --version

pip3 -m venv ./venv
source venv/bin/activate
docker-compose build
docker-compose up -d
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# install trivy
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy

# scan current dir
trivy fs .

# scan containers
trivy image jenkins
