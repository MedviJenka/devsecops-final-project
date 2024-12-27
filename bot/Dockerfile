ARG version=3.12-slim
FROM python:$version
WORKDIR /ai-server
ENV PYTHONPATH=/ai-server
COPY ../requirements.txt .
COPY ../.env .
RUN pip install --no-cache-dir -r requirements.txt
COPY bot /ai-server/bot
COPY core /ai-server/core
ENTRYPOINT ["python"]
CMD ["/ai-server/bot/server.py"]
