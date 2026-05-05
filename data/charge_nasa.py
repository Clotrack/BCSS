import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# Configuraciones de rutas (pathlib resuelve conflictos rutas linux y windows)
BASE_PATH = Path().resolve()
DATA_PROCESSED = BASE_PATH / "processed"

df_nasa = pd.read_csv(DATA_PROCESSED / "nasa_exoplanets_processed.csv")

df_nasa.to_sql("nasa_exoplanets", engine, if_exists="append", index=False)