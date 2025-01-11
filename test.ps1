#docker network create app-network
#
docker build -t medvijenia/app-base --target base -f app/Dockerfile .
docker build -t medvijenia/app-frontend --target frontend -f app/Dockerfile .
docker build -t medvijenia/app-backend --target backend -f app/Dockerfile .
#
#docker run -d --network app-network -p 89:89 app-frontend
#docker run -d --network app-network -p 88:88 -e OPENAI_API_KEY="" app-backend
#
#
## Define the URL
#$url = "http://backend:88/roast"
#
## Define the headers
#$headers = @{
#    "Content-Type" = "application/json"
#}
#
## Define the JSON payload
#$body = @{
#    "input" = "Why is AI smarter than humans?"
#} | ConvertTo-Json -Depth 10
#
## Send the POST request
#$response = Invoke-WebRequest -Uri $url -Method POST -Headers $headers -Body $body
#
## Display the response
#$response.Content


docker push medvijenia/app-base:latest
docker push medvijenia/app-frontend:latest
docker push medvijenia/app-backend:latest
