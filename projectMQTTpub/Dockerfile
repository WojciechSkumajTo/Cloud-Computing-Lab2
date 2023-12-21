# Użyj oficjalny obraz Pythona jako obrazu bazowego
FROM python:3.8-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki aplikacji do katalogu roboczego
COPY . /app

# Zainstaluj zależności
RUN pip install paho-mqtt

ENV PYTHONUNBUFFERED 1

# Uruchom komendę, aby uruchomić klienta MQTT publikującego
CMD ["python3", "/app/mqtt_pub_client.py"]
