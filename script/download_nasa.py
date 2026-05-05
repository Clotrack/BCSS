import requests
import pandas as pd
from io import StringIO
from pathlib import Path

# Conexion API NASA
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

# Seleccionar los datos relebantes
query = """
SELECT pl_name, hostname, ra, dec, sy_dist, pl_rade, pl_bmasse, pl_orbsmax
FROM ps
WHERE sy_dist < 65
"""

params = {
    "query": query,
    "format": "csv"
}

print("Descargando...")

response = requests.get(url, params=params)

# Comprobar la respuesta
print("Status code:", response.status_code)

data = StringIO(response.text)
df = pd.read_csv(data)

print("Filas:", len(df))

# Ruta basada en el script (NO en terminal)
base_path = Path(__file__).resolve().parent
output_path = base_path / ".." / "data" / "raw"

# Crear carpeta
output_path.mkdir(parents=True, exist_ok=True)

file_path = output_path / "nasa_exoplanets.csv"

# Guardar CSV
df.to_csv(file_path, index=False)

print("Archivo guardado en:")
print(file_path.resolve())