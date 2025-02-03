ARG python_version=3.12-alpine
ARG ubuntu_version=latest


FROM python:$python_version AS base
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
EXPOSE 89
ENTRYPOINT ["python"]
CMD ["main.py"]


FROM base AS backend
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
WORKDIR /app/backend
COPY /app/backend .
EXPOSE 88
ENTRYPOINT ["python"]
CMD ["server.py"]


FROM selenium/standalone-chrome AS tests
WORKDIR /tests
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY ../requirements.txt .
COPY ../tests .
RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/venv/bin/pytest"]
