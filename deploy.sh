#!/bin/bash
minikube start
minikube addons enable ingress
kubectl create secret generic openai-api-key --from-literal=OPENAI_API_KEY=""

MINIKUBE_IP=$(minikube ip)
ENTRY="$MINIKUBE_IP ai-bot.local.com"

if ! grep -qxF "$ENTRY" /etc/hosts; then
  echo "$ENTRY" | sudo tee -a /etc/hosts
  echo "Entry added: $ENTRY"
else
  echo "Entry already exists: $ENTRY"
fi
grep -qxF "$(minikube ip) ai-bot.local.com" /etc/hosts || echo "$(minikube ip) ai-bot.local.com" | sudo tee -a /etc/hosts

kubectl apply -f k8s/.
curl http://ai-bot.local.com/health
