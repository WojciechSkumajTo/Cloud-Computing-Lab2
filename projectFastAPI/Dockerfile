# Użyj obrazu bazowego Pythona
FROM python:3.9

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki z aktualnego katalogu do katalogu /app w kontenerze
COPY . /app

# Zainstaluj zależności
RUN pip install -r requirements.txt

# Zdefiniuj port, na którym będzie działać FastAPI
EXPOSE 8000

# Uruchom aplikację FastAPI
CMD ["uvicorn", "api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

