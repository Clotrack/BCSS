import time
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://user:password@db:5432/BCSS"

def wait_for_db():
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            with engine.connect() as conn:
                print("Conectado a la base de datos")
                return engine
        except Exception as e:
            print("Esperando a PostgreSQL...")
            time.sleep(2)

engine = wait_for_db()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

# Exponer datos de estrellas
@app.get("/stars")
def get_stars(limit: int = 100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM gaia_stars LIMIT :limit"),
            {"limit": limit}
        )
        return [dict(row._mapping) for row in result]
    
# Exponer datos de planetas
@app.get("/planets")
def get_planets(limit: int = 100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM nasa_exoplanets LIMIT :limit"),
            {"limit": limit}
        )
        return [dict(row._mapping) for row in result]
    
# Exponer relaciones entre estrellas (Gaia) y planetas (NASA)
@app.get("/matches")
def get_matches():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT *
            FROM star_match_planets
            LIMIT 100
        """))
        return [dict(row._mapping) for row in result]

# Exponer datos de estrellas curadas
@app.get("/stars_curated")
def get_stars_curated(limit: int = 100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM star_spectral_curated LIMIT :limit"),
            {"limit": limit}
        )
        return [dict(row._mapping) for row in result]

# Exponer datos de planetas curados
@app.get("/planets_curated")
def get_planets_curated(limit: int = 100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM planet_type_curated LIMIT :limit"),
            {"limit": limit}
        )
        return [dict(row._mapping) for row in result]
    
# Endpoint para la vista unificada
@app.get("/analysis")
def get_analysis(limit: int = 100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM v_Sanalisis_final LIMIT :limit"),
            {"limit": limit}
        )
        return [dict(row._mapping) for row in result]