ARG version=3.12-slim
FROM python:$version
WORKDIR /ai-server
COPY ../requirements.txt .
COPY ../.env .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/ai-server
COPY ai_engine /ai-server/ai_engine
COPY core /ai-server/core
ENTRYPOINT ["python"]
CMD ["/ai-server/ai_engine/server.py"]
