FROM ubuntu:latest
LABEL authors="Harish"

ENTRYPOINT ["top", "-b"]
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]