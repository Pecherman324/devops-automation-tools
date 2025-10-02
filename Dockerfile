# DevOps Automation Tools - Dockerfile
# Materia: Herramientas de Automatización en DevOps
# Profesor: Froylan Alonso Perez
# Alumno: Cesar Ulises Saldivar Chavez

# Usar imagen base de Python 3.11 slim
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    PORT=5000

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
ENV HOST=0.0.0.0
CMD ["python", "app.py"]
