from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = 'devops-automation-2024'

@app.route('/')
def index():
    """Página principal con información del proyecto"""
    return render_template('index.html')

@app.route('/api/info')
def api_info():
    """Endpoint API que retorna información del sistema"""
    return jsonify({
        'materia': 'Herramientas de Automatización en DevOps',
        'profesor': 'Froylan Alonso Perez',
        'alumno': 'Cesar Ulises Saldivar Chavez',
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'version': '1.0.0',
        'entorno': os.getenv('ENVIRONMENT', 'development'),
        'status': 'running'
    })

@app.route('/api/health')
def health_check():
    """Endpoint para verificación de salud de la aplicación"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime': 'running'
    })

@app.route('/api/version')
def version():
    """Endpoint que retorna la versión de la aplicación"""
    return jsonify({
        'version': '1.0.0',
        'build': os.getenv('BUILD_NUMBER', 'local'),
        'commit': os.getenv('GIT_COMMIT', 'unknown')
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
