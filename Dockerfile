ARG version=3.12-slim
FROM python:$version
WORKDIR /app
ENV PYTHONPATH=/app
COPY requirements.txt /app
COPY .env /app
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
EXPOSE 88
ENTRYPOINT ["python"]
CMD ["/app/app/main.py"]
