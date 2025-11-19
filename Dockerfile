FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install Flask==2.3.3

CMD ["python", "app.py"]
