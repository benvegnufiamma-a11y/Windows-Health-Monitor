# Windows-Health-Monitor
Script en Python para auditar el rendimiento del hardware (CPU, RAM, Disco) y generar logs automáticos
#  Script de Monitoreo de Salud de Windows (Python)

##  Sobre el Proyecto
Este es un script de automatización desarrollado en **Python** diseñado para equipos de Soporte IT y Administradores de Sistemas (SysAdmins). Su objetivo es auditar en tiempo real el consumo de recursos de hardware en máquinas con sistema operativo Windows y generar un archivo de registro (log) automatizado.

##  Características Principales
* **Lectura de CPU:** Mide el porcentaje exacto de carga del procesador.
* **Auditoría de RAM:** Calcula la memoria total instalada y el porcentaje de utilización actual.
* **Control de Almacenamiento:** Verifica el espacio total y libre en el disco principal (C:).
* **Generación de Logs:** Crea automáticamente un archivo `.txt` con la fecha, hora exacta y los resultados del escaneo para mantener un historial de rendimiento.

##  Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Librerías principales:** `psutil` (extracción de métricas de hardware), `platform` (datos del SO), `datetime` (marcas de tiempo).

##  Cómo ejecutarlo
1. Clonar este repositorio o descargar el archivo `Monitoreowindows.py`.
2. Instalar la dependencia necesaria ejecutando en la terminal: `pip install psutil`
3. Ejecutar el script con: `python Monitoreowindows.py`
