# Usamos una versión ligera de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos primero los requerimientos para aprovechar el caché de Docker
COPY app/requirements.txt .

# Instalamos las librerías financieras y de IA
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY app/ .

# Comando para iniciar FastAPI en el puerto 8001
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
