
docker build -t medvijenia/app-base --target base -f app/Dockerfile .
docker build -t medvijenia/app-frontend --target frontend -f app/Dockerfile .
docker build -t medvijenia/app-backend --target backend -f app/Dockerfile .
docker push medvijenia/app-base:latest
docker push medvijenia/app-frontend:latest
docker push medvijenia/app-backend:latest
