import psutil
import platform
from datetime import datetime

# 1. Obtenemos la fecha y hora actual
fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nombre_archivo = "Reporte_Salud.txt"

# 2. Abrimos (o creamos) un archivo de texto en modo escritura ('w')
with open(nombre_archivo, 'w') as archivo:
    archivo.write("=== REPORTE DE SALUD DEL SISTEMA ===\n")
    archivo.write(f"Fecha de ejecucion: {fecha_actual}\n")
    archivo.write(f"Sistema Operativo: {platform.system()} {platform.release()}\n\n")

    # CPU
    cpu_uso = psutil.cpu_percent(interval=1)
    archivo.write(f"[CPU] Uso actual: {cpu_uso}%\n")

    # Memoria RAM
    memoria = psutil.virtual_memory()
    archivo.write(f"[RAM] Total: {memoria.total / (1024**3):.2f} GB\n")
    archivo.write(f"[RAM] Usada: {memoria.percent}%\n")

    # Disco
    disco = psutil.disk_usage('C:')
    archivo.write(f"[DISCO C:] Total: {disco.total / (1024**3):.2f} GB | Libre: {disco.free / (1024**3):.2f} GB\n")

print(f"¡Éxito! Se ha generado el archivo {nombre_archivo} en tu carpeta.")