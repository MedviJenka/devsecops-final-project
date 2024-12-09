ARG version=3.12-slim

FROM python:$version

LABEL author="jenia petrusenko" description="DevSecOps Python project" version="1.0"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

COPY ai /app/ai
COPY core /app/core
COPY app /app/app

ENTRYPOINT ["python"]

CMD ["/app/app/main.py"]
