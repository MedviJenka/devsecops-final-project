ARG version=3.12-alpine
FROM python:$version AS base
WORKDIR /app
ENV PYTHONPATH=/app
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

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
