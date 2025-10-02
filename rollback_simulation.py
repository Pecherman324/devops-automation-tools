#!/usr/bin/env python3
"""
Simulación de Rollback para DevOps Automation
Este script simula un proceso de rollback en caso de fallo en producción

Materia: Herramientas de Automatización en DevOps
Profesor: Froylan Alonso Perez
Alumno: Cesar Ulises Saldivar Chavez
"""

import time
import json
import requests
from datetime import datetime
import subprocess
import sys

class RollbackSimulator:
    def __init__(self, app_url="http://localhost:5000"):
        self.app_url = app_url
        self.backup_versions = []
        
    def log(self, message):
        """Registrar mensajes con timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Reemplazar emojis por texto para compatibilidad con Windows
        message = message.replace("✅", "[OK]").replace("❌", "[ERROR]").replace("🚨", "[ALERTA]")
        message = message.replace("💾", "[BACKUP]").replace("🔄", "[ROLLBACK]").replace("📋", "[INFO]")
        message = message.replace("⚡", "[EJECUTANDO]").replace("🔍", "[VERIFICANDO]").replace("📊", "[ESTADO]")
        message = message.replace("🎯", "[INICIO]").replace("⚠️", "[ADVERTENCIA]").replace("🟢", "[FUNCIONANDO]")
        message = message.replace("🔴", "[PROBLEMAS]").replace("📦", "[VERSION]")
        print(f"[{timestamp}] {message}")
        
    def check_application_health(self):
        """Verificar el estado de salud de la aplicación"""
        try:
            response = requests.get(f"{self.app_url}/api/health", timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.log(f"✅ Aplicación saludable: {data['status']}")
                return True
            else:
                self.log(f"❌ Aplicación no saludable: Status {response.status_code}")
                return False
        except requests.RequestException as e:
            self.log(f"❌ Error conectando a la aplicación: {e}")
            return False
            
    def get_current_version(self):
        """Obtener la versión actual de la aplicación"""
        try:
            response = requests.get(f"{self.app_url}/api/version", timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.log(f"📋 Versión actual: {data['version']} (Build: {data['build']})")
                return data
            else:
                self.log(f"❌ No se pudo obtener la versión: Status {response.status_code}")
                return None
        except requests.RequestException as e:
            self.log(f"❌ Error obteniendo versión: {e}")
            return None
            
    def simulate_deployment_failure(self):
        """Simular un fallo en el despliegue"""
        self.log("🚨 SIMULANDO FALLO EN DESPLIEGUE...")
        self.log("   - Nueva versión con errores críticos")
        self.log("   - Aplicación no responde correctamente")
        self.log("   - Errores 500 en endpoints principales")
        time.sleep(2)
        
    def create_backup_version(self):
        """Crear una versión de respaldo"""
        current_version = self.get_current_version()
        if current_version:
            backup = {
                'version': current_version['version'],
                'build': current_version['build'],
                'commit': current_version['commit'],
                'timestamp': datetime.now().isoformat(),
                'status': 'backup'
            }
            self.backup_versions.append(backup)
            self.log(f"💾 Backup creado: Versión {backup['version']}")
            return backup
        return None
        
    def execute_rollback(self):
        """Ejecutar el proceso de rollback"""
        self.log("🔄 INICIANDO PROCESO DE ROLLBACK...")
        
        if not self.backup_versions:
            self.log("❌ No hay versiones de respaldo disponibles")
            return False
            
        # Obtener la última versión de respaldo
        last_backup = self.backup_versions[-1]
        self.log(f"📦 Revirtiendo a versión: {last_backup['version']}")
        
        # Simular comandos de rollback
        rollback_commands = [
            "docker stop devops-app",
            "docker rm devops-app", 
            f"docker run -d -p 5000:5000 --name devops-app devops-automation-app:{last_backup['version']}",
            "sleep 10",  # Esperar a que el contenedor inicie
        ]
        
        for command in rollback_commands:
            self.log(f"⚡ Ejecutando: {command}")
            time.sleep(1)  # Simular tiempo de ejecución
            
        # Verificar que el rollback fue exitoso
        time.sleep(5)
        if self.check_application_health():
            self.log("✅ ROLLBACK EXITOSO")
            self.log(f"   - Aplicación restaurada a versión {last_backup['version']}")
            self.log(f"   - Estado: Funcionando correctamente")
            return True
        else:
            self.log("❌ ROLLBACK FALLIDO")
            self.log("   - La aplicación sigue sin funcionar")
            self.log("   - Se requiere intervención manual")
            return False
            
    def run_simulation(self):
        """Ejecutar la simulación completa de rollback"""
        self.log("🎯 INICIANDO SIMULACIÓN DE ROLLBACK")
        self.log("=" * 50)
        
        # Paso 1: Verificar estado inicial
        self.log("📊 Verificando estado inicial de la aplicación...")
        if not self.check_application_health():
            self.log("❌ La aplicación no está funcionando. Abortando simulación.")
            return False
            
        # Paso 2: Crear backup de la versión actual
        self.log("\n💾 Creando backup de la versión actual...")
        backup = self.create_backup_version()
        if not backup:
            self.log("❌ No se pudo crear backup. Abortando simulación.")
            return False
            
        # Paso 3: Simular fallo en despliegue
        self.log("\n🚨 Simulando fallo en nuevo despliegue...")
        self.simulate_deployment_failure()
        
        # Paso 4: Verificar que la aplicación falló
        self.log("\n🔍 Verificando fallo de la aplicación...")
        if self.check_application_health():
            self.log("⚠️ La aplicación sigue funcionando. Simulando fallo...")
            time.sleep(2)
            
        # Paso 5: Ejecutar rollback
        self.log("\n🔄 Ejecutando rollback...")
        rollback_success = self.execute_rollback()
        
        # Paso 6: Resumen final
        self.log("\n" + "=" * 50)
        self.log("📋 RESUMEN DE LA SIMULACIÓN")
        self.log(f"   - Backup creado: {backup['version']}")
        self.log(f"   - Rollback ejecutado: {'✅ Exitoso' if rollback_success else '❌ Fallido'}")
        self.log(f"   - Estado final: {'🟢 Aplicación funcionando' if rollback_success else '🔴 Aplicación con problemas'}")
        
        return rollback_success

def main():
    """Función principal"""
    print("Simulador de Rollback - DevOps Automation")
    print("=" * 50)
    
    simulator = RollbackSimulator()
    
    try:
        success = simulator.run_simulation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️ Simulación interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error durante la simulación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
