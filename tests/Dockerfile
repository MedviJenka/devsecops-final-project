ARG version=3.12-slim
FROM python:$version
WORKDIR /tests
COPY /tests ./tests
COPY /core ./core
COPY /app ./app
COPY ../requirements.txt /tests
COPY ../.env /tests
ENV PYTHONPATH=/tests
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["pytest"]
CMD ["/tests/tests/test_requests.py"]
