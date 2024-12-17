ARG version=3.12-slim
FROM python:$version
LABEL author="jenia petrusenko" description="DevSecOps Python project" version="1.0"
WORKDIR /app
ENV PYTHONPATH=/app
COPY ../requirements.txt /app
COPY ../.env /app
RUN pip install --no-cache-dir -r requirements.txt
COPY /app ./app
ENTRYPOINT ["python"]
CMD ["/app/app/main.py"]
