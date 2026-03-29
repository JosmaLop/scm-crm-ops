# Usa una imagen oficial de Python ligera
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la API
COPY . /app

# Instalar dependencias
RUN pip install flask mysql-connector-python pandas openpyxl

# Exponer el puerto de la API
EXPOSE 5000

# Comando para iniciar la API
CMD ["python", "api.py"]