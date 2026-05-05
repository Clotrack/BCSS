from sqlalchemy import create_engine, text

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

query = """
INSERT INTO star_match_planets (source_id, nasa_exoplanet_id, match_distance, match_confidence)
SELECT DISTINCT ON (n.nasa_exoplanet_id)
    g.source_id,
    n.nasa_exoplanet_id,
    SQRT(POWER(g.ra - n.ra, 2) + POWER(g.dec - n.dec, 2)) AS match_distance,
    1 / (1 + SQRT(POWER(g.ra - n.ra, 2) + POWER(g.dec - n.dec, 2))) AS match_confidence
FROM gaia_stars g
JOIN nasa_exoplanets n
ON ABS(g.ra - n.ra) < 0.01 AND ABS(g.dec - n.dec) < 0.01
ORDER BY n.nasa_exoplanet_id, match_distance ASC;
"""

with engine.connect() as conn:
    conn.execute(text(query))
    conn.commit()