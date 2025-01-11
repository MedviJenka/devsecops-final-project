#!/bin/bash

minikube start
minikube addons enable ingress
kubectl create secret generic openai-api-key --from-literal=OPENAI_API_KEY=""

MINIKUBE_IP=$(minikube ip)
ENTRY="$MINIKUBE_IP bot.k8s.com"

if ! grep -qxF "$ENTRY" /etc/hosts; then
  echo "$ENTRY" | sudo tee -a /etc/hosts
  echo "Entry added: $ENTRY"
else
  echo "Entry already exists: $ENTRY"
fi

grep -qxF "$(minikube ip) bot.k8s.com" /etc/hosts || echo "$(minikube ip) bot.k8s.com" | sudo tee -a /etc/hosts

kubectl apply -f k8s/.

curl http://bot.k8s.com/health
