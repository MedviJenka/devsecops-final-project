ARG version=3.12-slim
FROM python:$version
WORKDIR /tests
ENV PYTHONPATH=/tests
COPY /tests ./tests
COPY /core ./core
COPY /app ./app
COPY ../requirements.txt /tests
COPY ../.env /tests
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "/tests", "--alluredir", "/tests/results"]
