sudo
minikube start
echo "$(minikube ip) ai-bot.local.com" >> ~/etc/hosts
kubectl apply -f .
curl http://ai-bot.local.com/health