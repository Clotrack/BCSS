import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# Configuraciones de rutas (pathlib resuelve conflictos rutas linux y windows)
BASE_PATH = Path().resolve()
DATA_CURATED = BASE_PATH / "curated"

df_planet = pd.read_csv(DATA_CURATED / "planet_type_curated.csv")

df_planet.to_sql("planet_type_curated", engine, if_exists="append", index=False)

print("Cargados datos de planetas exitosamente.")

df_stars = pd.read_csv(DATA_CURATED / "star_spectral_curated.csv")

df_stars.to_sql("star_spectral_curated", engine, if_exists="append", index=False)

print("Cargados datos de estrellas exitosamente.")