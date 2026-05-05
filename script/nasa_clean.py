import pandas as pd
from pathlib import Path

BASE_PATH = Path().resolve()
DATA_RAW = BASE_PATH / ".." / "data" / "raw"
DATA_PROCESSED = BASE_PATH / ".." / "data" / "processed"

DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

file_path = DATA_RAW / "nasa_exoplanets.csv"

df = pd.read_csv(file_path)

# Comprobaciones de valores duplicados, absurdos o fuera de rango
# Nombres duplicados de planetas?
df["pl_name"] = (
    df["pl_name"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# Nombres duplicados de estrellas?
df["hostname"] = (
    df["hostname"]
    .astype(str)
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

# Realizar media de datos con planetas duplicados
df = df.groupby("pl_name").agg({
    "hostname": "first",
    "ra": "mean",
    "dec": "mean",
    "sy_dist": "mean",
    "pl_rade": "mean",
    "pl_bmasse": "mean",
    "pl_orbsmax": "mean"
}).reset_index()

# Se eliminan duplicados por nombre de planeta para asegurar
df = df.drop_duplicates(subset=["pl_name"])

# RA
df = df[(df["ra"] >= 0) & (df["ra"] <= 360)]
print("Tras filtro RA:", len(df))

# DEC
df = df[(df["dec"] >= -90) & (df["dec"] <= 90)]
print("Tras filtro DEC:", len(df))

# Distancia
df = df[df["sy_dist"] > 0]
print("Tras filtro distancia:", len(df))

# Procedemos a guardar
output_path = DATA_PROCESSED / "nasa_exoplanets_processed.csv"

df.to_csv(output_path, index=False)

print("Guardado en:", output_path)