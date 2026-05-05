from sqlalchemy import create_engine, Column, Float, BigInteger, Integer, Text, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Cambia los credenciales si es necesario
engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# --- TABLA CURATED DE ESTRELLAS ---
class StarSpectralCurated(Base):
    __tablename__ = "star_spectral_curated"

    # Usamos el source_id original como Primary Key
    source_id = Column(BigInteger, primary_key=True)
    abs_mag = Column(Float)
    bp_rp = Column(Float)
    spectral_type = Column(Text)
    distance_pc = Column(Float)
    estimated_mass = Column(Float)
    is_sun_like = Column(Boolean)

# --- TABLA CURATED DE PLANETAS ---
class PlanetTypeCurated(Base):
    __tablename__ = "planet_type_curated"

    # Aquí el ID viene del merge que hiciste con la tabla original
    nasa_exoplanet_id = Column(Integer, primary_key=True)
    pl_name = Column(Text)
    hostname = Column(Text)
    pl_rade = Column(Float)
    pl_bmasse = Column(Float)
    pl_orbsmax = Column(Float)
    sy_dist = Column(Float)
    planet_type = Column(Text)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)
print("Tablas 'curated' creadas exitosamente.")