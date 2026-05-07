import subprocess
import sys
import time

def run_script(script_name):
    header = f" EJECUTANDO: {script_name} "
    # Línea decorativa del mismo ancho que el mensaje
    border = "=" * len(header)
    
    print(f"\n{border}")
    print(header)
    print(f"{border}\n")

    try:
        # Ejecuta el script y espera a que termine
        result = subprocess.run([sys.executable, script_name], check=True)
        
        # Línea de cierre
        footer = f"{script_name} finalizado con éxito "
        print(f"\n{footer}")
        print("-" * len(footer))
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ ERROR CRÍTICO en {script_name}")
        print(f"Detalles: {e}")
        print("!" * 50)
        sys.exit(1)

def main():
    print("INICIANDO PIPELINE DEL PROYECTO BCSS CRUCEMOS LOS DEDOS...\n")

    # 1. Crear las tablas base
    run_script("data/createBBDD_estructure.py")

    # Procesos ETL
    # 2. Cargar datos en Raw (Ingesta) Conectarse y descargar datos de la NASA
    run_script("script/download_nasa.py")

    # 3. Procesamos los datos y los guardamos en Processed
    run_script("script/gaia_clean.py")
    run_script("script/nasa_clean.py")

    # 4. Guardamos los datos en Postgres
    run_script("data/charge_gaia.py")
    run_script("data/charge_nasa.py")
    run_script("data/charge_match.py")

    # Procesos EDA y generación de archivos Curated
    # 5. Asegúrate de que tus notebooks estén convertidos a .py o usa scripts
    run_script("script/stars_eda.py")
    run_script("script/planets_eda.py")

    # 6. Cargar datos Curated en Postgres
    run_script("data/charge_curated.py")

    # 7. Crear la Vista SQL
    run_script("data/create_view.py")

    print("TODO EL SISTEMA ESTÁ ASIMILADO, SOMOS BORG")
    print("Puedes acceder a la API en el puerto 8000 y a Grafana en el 3000.")

if __name__ == "__main__":
    main()