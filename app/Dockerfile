ARG version=3.12-alpine
FROM python:$version AS base
WORKDIR /app
ENV PYTHONPATH=/app
COPY ../requirements.txt .
COPY ../. .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ../.env .

FROM base AS frontend
WORKDIR /app/frontend
COPY /app/frontend .
ENTRYPOINT ["python"]
CMD ["main.py"]

FROM base AS backend
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
WORKDIR /app/backend
COPY /app/backend .
ENTRYPOINT ["python"]
CMD ["server.py"]

FROM base AS jenkins
