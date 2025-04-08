FROM python:3.11-slim

WORKDIR /app

COPY frontend/ /app/frontend


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["python", "app.py"]

