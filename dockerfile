FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y default-mysql-client

COPY API/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY API /app/
COPY API/ssl /app/ssl

EXPOSE 443

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "443", "--ssl-keyfile", "/app/ssl/key.pem", "--ssl-certfile", "/app/ssl/cert.pem"]
