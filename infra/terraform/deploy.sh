#!/bin/bash
set -e

# Update system and install prerequisites
yum update -y
yum install -y docker git curl

# Start and configure Docker
service docker start
usermod -a -G docker ec2-user

# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Clone the Git repository
git clone ${git_repo_url} /home/ec2-user/devsecops-final-project

# Switch to the ec2-user
su - ec2-user << EOF_USER

# Start Minikube
minikube start --driver=docker

# Configure Kubernetes
mkdir -p /home/ec2-user/.kube
cp /etc/kubernetes/admin.conf /home/ec2-user/.kube/config
chown ec2-user:ec2-user /home/ec2-user/.kube/config

# Apply a CNI plugin (Flannel)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# Deploy Kubernetes manifests
kubectl apply -f /home/ec2-user/devsecops-final-project/${k8s_manifest_path}

EOF_USER
