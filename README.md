# DevOps Automation Tools

## Descripción del Proyecto

Proyecto final de la materia "Herramientas de Automatización en DevOps" que implementa un pipeline completo de automatización con contenerización, CI/CD y sistema de rollback.

## Características

- ✅ Aplicación Flask con interfaz web
- ✅ Contenerización con Docker
- ✅ Pipeline CI/CD con GitHub Actions
- ✅ Sistema de rollback automatizado
- ✅ Pruebas unitarias

## Estructura del Proyecto

```
proyecto_final/
├── app.py                          # Aplicación Flask principal
├── requirements.txt                # Dependencias de Python
├── Dockerfile                      # Configuración de Docker
├── docker-compose.yml              # Orquestación de servicios
├── test_app.py                     # Pruebas unitarias
├── pytest.ini                     # Configuración de pytest
├── rollback_simulation.py          # Simulador de rollback
├── .github/workflows/ci.yml        # Pipeline CI/CD
├── templates/
│   └── index.html                  # Interfaz web
├── REPORTE_DEVOPS_AUTOMATION.md    # Reporte completo
└── README.md                       # Este archivo
```

## Instalación y Uso

### Prerrequisitos

- Python 3.11+
- Docker
- Git

### Instalación Local

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd proyecto_final
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
python app.py
```

4. Acceder a la aplicación:
- Web: http://localhost:5000
- API Health: http://localhost:5000/api/health
- API Info: http://localhost:5000/api/info
- API Version: http://localhost:5000/api/version

### Uso con Docker

1. Construir la imagen:
```bash
docker build -t devops-automation-app .
```

2. Ejecutar el contenedor:
```bash
docker run -d -p 5000:5000 --name devops-app devops-automation-app
```

3. Verificar el funcionamiento:
```bash
curl http://localhost:5000/api/health
```

### Uso con Docker Compose

1. Ejecutar todos los servicios:
```bash
docker-compose up -d
```

2. Verificar el estado:
```bash
docker-compose ps
```

## Pruebas

### Ejecutar Pruebas Unitarias
```bash
pytest test_app.py -v
```

### Análisis de Código
```bash
# Ejecutar pruebas con cobertura
python -m pytest test_app.py -v
```

## Simulación de Rollback

Ejecutar la simulación de rollback:
```bash
python rollback_simulation.py
```

## Pipeline CI/CD

El pipeline de CI/CD está configurado en `.github/workflows/ci.yml` e incluye:

1. **Pruebas Unitarias**: Pytest
2. **Construcción**: Docker image build
3. **Despliegue**: Automático a producción
4. **Verificación**: Health check post-despliegue
5. **Rollback**: Automático en caso de fallo

## Monitoreo

### Health Checks
- Endpoint: `/api/health`
- Estado de la aplicación en tiempo real

## Contribución

1. Fork el proyecto
2. Crear una rama para la feature (`git checkout -b feature/AmazingFeature`)
3. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

- **Alumno**: Cesar Ulises Saldivar Chavez
- **Materia**: Herramientas de Automatización en DevOps
- **Profesor**: Froylan Alonso Perez

## Agradecimientos

- Flask por el framework web
- Docker por la contenerización
- GitHub Actions por la automatización CI/CD
- Comunidad DevOps por las mejores prácticas
