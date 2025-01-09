3. Writing the Dockerfile
Create a Dockerfile to containerize the application.

Dockerfile
Copy code
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 88

CMD ["python", "/app/main.py"]
4. Build and Push the Docker Image
Build the Docker image:
bash
Copy code
docker build -t python-ai-app .
Test the image locally:
bash
Copy code
docker run -p 88:88 -e OPENAI_API_KEY=<your-api-key> python-ai-app
Push the image to a container registry (e.g., Docker Hub):
bash
Copy code
docker tag python-ai-app <your-dockerhub-username>/python-ai-app:latest
docker push <your-dockerhub-username>/python-ai-app:latest
5. Kubernetes Deployment
5.1 Create a Kubernetes Secret
Store the OpenAI API key securely in Kubernetes:

bash
Copy code
kubectl create secret generic openai-api-key --from-literal=OPENAI_API_KEY=<your-api-key>
5.2 Deployment Manifest
Create a deployment.yaml:

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-ai-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-ai-app
  template:
    metadata:
      labels:
        app: python-ai-app
    spec:
      containers:
      - name: python-ai-app
        image: <your-dockerhub-username>/python-ai-app:latest
        ports:
        - containerPort: 88
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: openai-api-key
              key: OPENAI_API_KEY
5.3 Service Manifest
Create a service.yaml:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: python-ai-app-service
spec:
  selector:
    app: python-ai-app
  ports:
    - protocol: TCP
      port: 88
      targetPort: 88
  type: NodePort
5.4 Apply Manifests
Deploy the application:

bash
Copy code
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
6. Access the Application
6.1 Get Minikube IP
bash
Copy code
minikube ip
6.2 Access the Application
Use the NodePort (e.g., 30088) to access the application:

bash
Copy code
http://<minikube-ip>:30088
6.3 Debugging
If the application doesn’t respond:

Check pod logs:
bash
Copy code
kubectl logs <pod-name>
Verify service:
bash
Copy code
kubectl describe service python-ai-app-service
7. Bonus: Using Ingress
Enable Ingress for user-friendly URLs:

bash
Copy code
minikube addons enable ingress
Create an ingress.yaml:

yaml
Copy code

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: python-ai-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: python-ai-app.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: python-ai-app-service
            port:
              number: 88
```


Apply the Ingress:

bash
Copy code
kubectl apply -f ingress.yaml
Edit /etc/hosts to map the domain:

plaintext
Copy code
<minikube-ip> python-ai-app.local
Access the app:

bash
Copy code
http://python-ai-app.local
8. Clean Up
To delete the resources:

bash
Copy code
kubectl delete deployment python-ai-app
kubectl delete service python-ai-app-service
kubectl delete secret openai-api-key
kubectl delete ingress python-ai-app-ingress
minikube stop