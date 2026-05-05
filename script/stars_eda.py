import pandas as pd
import numpy as np
from pathlib import Path

# Configuraciones de rutas (pathlib resuelve conflictos rutas linux y windows)
BASE_PATH = Path().resolve()
DATA_PROCESSED = BASE_PATH / ".." / "data" / "processed"
DATA_CURATED = BASE_PATH / ".." / "data" / "curated"

DATA_CURATED.mkdir(parents=True, exist_ok=True)

file_path = DATA_PROCESSED / "gaia_neighbor_processed.csv"

# Lectura del arcchivo csv rawprocessed
df = pd.read_csv(file_path)

# Calcular Magnitud Absoluta y crear columna
df['abs_mag'] = df['phot_g_mean_mag'] - 5 * np.log10(df['distance_pc']) + 5

# Clasificar por tipo espectral
def classify_spectral(color):
    if color < -0.3: return 'O'
    if color < 0.0: return 'B'
    if color < 0.3: return 'A'
    if color < 0.8: return 'F'
    if color < 1.15: return 'G'
    if color < 1.6: return 'K'
    return 'M'
# Crear columna para tipo espectral
df['spectral_type'] = df['bp_rp'].apply(classify_spectral)

# Estimación de Masa y crear columna (esta es una aproximación para Secuencia Principal)
df['estimated_mass'] = 10**((4.75 - df['abs_mag']) / 10)

# Flag "Parecida al Sol" (Tipo G y Magnitud Absoluta entre 4 y 5.5)
df['is_sun_like'] = (df['spectral_type'] == 'G') & (df['abs_mag'].between(4, 5.5))

# Selección de variables para archivo curated
columns_to_keep = [
    'source_id', 'abs_mag', 'bp_rp', 
    'spectral_type', 'distance_pc', 
    'estimated_mass', 'is_sun_like'
]

df_stars_type_curated = df[columns_to_keep].copy()

# Guardado final
output_path = DATA_CURATED / "star_spectral_curated.csv"
df_stars_type_curated.to_csv(output_path, index=False)

print(f"Archivo Gaia guardado en: {output_path}")
print(f"Resumen: {len(df_stars_type_curated)} estrellas procesadas.")