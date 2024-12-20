#!/bin/bash

# update system
sudo apt-get update
sudo apt install docker docker.io

# install trivy
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy

# check versions
docker --version
docker-compose --version
trivy --version

# build image
docker-compose build jenkins

# scan image
trivy image jenkins

# run image
docker compose up -d jenkins

# get jenkins password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

# make it executable
run_jenkins_container.sh
