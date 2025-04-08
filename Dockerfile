FROM python:3.11-slim

WORKDIR /backend

COPY backend/ /backend


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]


