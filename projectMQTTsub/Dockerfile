# Dockerfile for MQTT subscriber client
FROM python:3.9

WORKDIR /app

# Kopiuj plik wymagany do subskrybowania
COPY mqtt_subscriber.py /app/

# Instaluj zależności
RUN pip install paho-mqtt httpx

# Ustaw zmienną środowiskową
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /app


CMD ["python3", "/app/mqtt_subscriber.py"]
