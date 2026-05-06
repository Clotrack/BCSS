import pandas as pd
from pathlib import Path

# __file__ es la ubicación de este script (gaia_clean.py)
# .parent nos sube a la carpeta 'script'
# .parent de nuevo nos sube a la raíz 'proyectoBCSS'
BASE_PATH = Path(__file__).resolve().parent.parent

# Ahora las rutas serán sólidas como una roca
DATA_RAW = BASE_PATH / "data" / "raw"
DATA_PROCESSED = BASE_PATH / "data" / "processed"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

file_path = DATA_RAW / "neighbor_stars.csv"

# Lectura del arcchivo csv raw
df = pd.read_csv(file_path)

# Limpieza de posibles duplicados
df = df.drop_duplicates(subset=["source_id"])

# Comprobaciones de datos absurdos o fuera de rango
# RA
df = df[(df["ra"] >= 0) & (df["ra"] <= 360)]
# DEC
df = df[(df["dec"] >= -90) & (df["dec"] <= 90)]
# Distancias
df = df[df["parallax"] > 0]
df = df[df["parallax_over_error"] > 5]

# Fila añadida para futuras comparaciones con NASA
df["distance_pc"] = 1000 / df["parallax"]

# Procedemos a guardar
output_path = DATA_PROCESSED / "gaia_neighbor_processed.csv"

df.to_csv(output_path, index=False)

print(f"Archivo Gaia guardado en: {output_path}")
print(f"Resumen: {len(df)} estrellas procesadas.")