# Importanciónes y dependencias
import pandas as pd
import numpy as np
from pathlib import Path
from sqlalchemy import create_engine, text

# __file__ es la ubicación de este script (gaia_clean.py)
# .parent nos sube a la carpeta 'script'
# .parent de nuevo nos sube a la raíz 'proyectoBCSS'
BASE_PATH = Path(__file__).resolve().parent.parent

DATA_PROCESSED = BASE_PATH / "data" / "processed"
DATA_CURATED = BASE_PATH / "data" / "curated"

DATA_CURATED.mkdir(parents=True, exist_ok=True)

file_path = DATA_PROCESSED / "nasa_exoplanets_processed.csv"

# Lectura del arcchivo csv rawprocessed
df = pd.read_csv(file_path)

# Función de clasificación basada en Radio (más confiable que masa en exoplanetas)
def classify_planet(row):
    r = row['pl_rade']
    if pd.isna(r): return 'Unknown'
    if r < 1.25: return 'Terrestre'
    if r < 2.0:  return 'Super-Tierra'
    if r < 6.0:  return 'Neptuniano'
    return 'Gigante Gaseoso'

df['planet_type'] = df.apply(classify_planet, axis=1)

# Selección de columnas (sin el ID, que lo pondrá Postgres)
cols = [
    'pl_name', 'hostname', 
    'pl_rade', 'pl_bmasse', 
    'pl_orbsmax', 'sy_dist', 
    'planet_type'
]

df_planets_curated = df[cols].copy()

# Conexión con la base de datos
engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# 1. Obtener los IDs actuales de la DB
df_original = pd.read_sql("SELECT nasa_exoplanet_id, pl_name FROM nasa_exoplanets", engine)

# 2. Unir dataframes para obtener el id de la tabla nasa_exoplanets es esta
df_final = pd.merge(df_planets_curated, df_original, on='pl_name', how='left')

# Guardar final
output_path = DATA_CURATED / "planet_type_curated.csv"
df_final.to_csv(output_path, index=False)

print(f"Archivo NASA guardado en: {output_path}")
print(f"Resumen: {len(df_final)} planetas procesadas.")