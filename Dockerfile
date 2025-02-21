# Använd en officiell Python-baserad image
FROM python:3.9-slim

# Ställ in arbetskatalogen i containern
WORKDIR /app

# Kopiera requirements.txt och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera resten av projektfilerna
COPY . .

# Exponera porten som FastAPI kör på (vanligtvis 8000)
EXPOSE 8000

# Kör FastAPI-appen när containern startar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]