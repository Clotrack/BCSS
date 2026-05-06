import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# Configuraciones de rutas (pathlib resuelve conflictos rutas linux y windows)
BASE_PATH = Path(__file__).resolve().parent

DATA_RAW = BASE_PATH / "raw"
DATA_PROCESSED = BASE_PATH / "processed"

df_gaia = pd.read_csv(DATA_PROCESSED / "gaia_neighbor_processed.csv")

df_gaia.to_sql("gaia_stars", engine, if_exists="append", index=False)

print("Datos cargados exitosamente.")