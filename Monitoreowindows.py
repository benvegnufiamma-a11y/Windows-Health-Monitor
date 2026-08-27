import psutil
import platform
from datetime import datetime

# 1. Obtenemos la fecha y hora actual
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nombre_archivo = "Reporte_Salud.txt"

# 2. Abrimos el archivo de texto en modo escritura (con soporte para tildes)
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write("=== REPORTE DE SALUD DEL SISTEMA ===\n")
    archivo.write(f"Fecha de ejecución: {fecha_actual}\n")
    archivo.write(f"Sistema Operativo: {platform.system()} {platform.release()}\n\n")

    # --- CPU ---
    cpu_uso = psutil.cpu_percent(interval=1)
    archivo.write(f"[CPU] Uso actual: {cpu_uso}%\n")

    # --- Memoria RAM ---
    memoria = psutil.virtual_memory()
    ram_total_gb = memoria.total / (1024**3)
    ram_usada_gb = memoria.used / (1024**3)  # Aquí calculamos los GB usados
    
    archivo.write(f"[RAM] Total: {ram_total_gb:.2f} GB\n")
    archivo.write(f"[RAM] Usada: {ram_usada_gb:.2f} GB ({memoria.percent}%)\n")
    
    # ALERTA DE RAM: Si el porcentaje es mayor a 75
    if memoria.percent > 75:
        archivo.write("   ⚠️ ALERTA CRÍTICA: El uso de la memoria RAM superó el 75%.\n")

    # --- Disco Duro (C:) ---
    disco = psutil.disk_usage('C:')
    disco_total_gb = disco.total / (1024**3)
    disco_libre_gb = disco.free / (1024**3)
    
    archivo.write(f"[DISCO C:] Total: {disco_total_gb:.2f} GB | Libre: {disco_libre_gb:.2f} GB\n")
    
    # ALERTA DE DISCO: Si el espacio libre es menor a 20 GB
    if disco_libre_gb < 20:
        archivo.write("   ⚠️ ALERTA CRÍTICA: Queda muy poco espacio libre en el Disco C (Menos de 20 GB).\n")

print(f"¡Éxito! Se ha generado el archivo {nombre_archivo} con el nuevo sistema de alertas.")
