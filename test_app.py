"""
Pruebas unitarias para DevOps Automation Tools

Materia: Herramientas de Automatización en DevOps
Profesor: Froylan Alonso Perez
Alumno: Cesar Ulises Saldivar Chavez
"""

import pytest
import json
from app import app

@pytest.fixture
def client():
    """Crear cliente de prueba para la aplicación Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Probar que la página principal carga correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Automation Tools' in response.data

def test_api_info(client):
    """Probar el endpoint de información de la API"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'materia' in data
    assert 'profesor' in data
    assert 'alumno' in data
    assert 'version' in data
    assert data['status'] == 'running'

def test_health_check(client):
    """Probar el endpoint de verificación de salud"""
    response = client.get('/api/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'uptime' in data

def test_version_endpoint(client):
    """Probar el endpoint de versión"""
    response = client.get('/api/version')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'version' in data
    assert 'build' in data
    assert 'commit' in data

def test_nonexistent_endpoint(client):
    """Probar que los endpoints inexistentes devuelven 404"""
    response = client.get('/api/nonexistent')
    assert response.status_code == 404

if __name__ == '__main__':
    pytest.main([__file__])

