from sqlalchemy import create_engine, text

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

view_sql = """
CREATE VIEW v_Sanalisis_final AS
SELECT 
    s.source_id AS gaia_id,
    s.spectral_type,
    s.abs_mag,
    s.estimated_mass,
    s.is_sun_like,
    p.pl_name,
    p.planet_type,
    p.pl_orbsmax,
    p.sy_dist,
    m.match_distance
FROM star_match_planets m
JOIN star_spectral_curated s ON m.source_id = s.source_id
JOIN planet_type_curated p ON m.nasa_exoplanet_id = p.nasa_exoplanet_id;
"""

with engine.connect() as conn:
    conn.execute(text(view_sql))
    conn.commit()
    print("Vista 'v_analisis_final' creada correctamente.")