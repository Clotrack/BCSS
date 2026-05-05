from sqlalchemy import create_engine, Column, Float, BigInteger, Integer, Text, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

# TABLA DE ESTRELLAS
class GaiaStar(Base):
    __tablename__ = "gaia_stars"

    source_id = Column(BigInteger, primary_key=True)
    ra = Column(Float)
    dec = Column(Float)
    parallax = Column(Float)
    parallax_over_error = Column(Float)
    phot_g_mean_mag = Column(Float)
    bp_rp = Column(Float)
    distance_pc = Column(Float)

# TABLA DE PLANETAS
class NasaExoplanet(Base):
    __tablename__ = "nasa_exoplanets"

    nasa_exoplanet_id = Column(Integer, primary_key=True, autoincrement=True)
    pl_name = Column(Text)
    hostname = Column(Text)
    ra = Column(Float)
    dec = Column(Float)
    sy_dist = Column(Float)
    pl_rade = Column(Float)
    pl_bmasse = Column(Float)
    pl_orbsmax = Column(Float)

# TABLA MATCH DE PLANETAS Y ESTRELLAS
class StarMatch(Base):
    __tablename__ = "star_match_planets"

    star_match_id = Column(Integer, primary_key=True, autoincrement=True)
    source_id = Column(BigInteger, ForeignKey("gaia_stars.source_id"))
    nasa_exoplanet_id = Column(Integer, ForeignKey("nasa_exoplanets.nasa_exoplanet_id"))
    match_distance = Column(Float)
    match_confidence = Column(Float)

# TABLA CURATED DE ESTRELLAS
class StarSpectralCurated(Base):
    __tablename__ = "star_spectral_curated"

    # Usamos el source_id original como Primary Key!!!
    source_id = Column(BigInteger, primary_key=True)
    abs_mag = Column(Float)
    bp_rp = Column(Float)
    spectral_type = Column(Text)
    distance_pc = Column(Float)
    estimated_mass = Column(Float)
    is_sun_like = Column(Boolean)

# TABLA CURATED DE PLANETAS
class PlanetTypeCurated(Base):
    __tablename__ = "planet_type_curated"

    # Aquí el ID viene del merge de la tabla original!!!!
    nasa_exoplanet_id = Column(Integer, primary_key=True)
    pl_name = Column(Text)
    hostname = Column(Text)
    pl_rade = Column(Float)
    pl_bmasse = Column(Float)
    pl_orbsmax = Column(Float)
    sy_dist = Column(Float)
    planet_type = Column(Text)

Base.metadata.create_all(engine)

print("Tablas creadas exitosamente.")