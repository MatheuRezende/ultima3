# Dockerfile
FROM python:3.11-slim

WORKDIR /backend

COPY backend/ /backend/
COPY frontend/ /backend/frontend/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
