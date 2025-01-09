kubectl apply -f secret.yaml
kubectl create deployment openai-app --image="medvijenia/simple-app:1.0"
kubectl scale deployment openai --replicas=3
kubectl expose deployment openai-app --type=NodePort --port=88
minikube service app --url
