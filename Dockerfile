# Usamos una versión ligera de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos primero (optimiza la caché de Docker)
COPY main.py .

# Instalamos las librerías necesarias directamente
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy

# Exponemos el puerto 8000
EXPOSE 8000

# Comando para arrancar la API
# Usamos 0.0.0.0 para que sea accesible desde fuera del contenedor (Android)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]