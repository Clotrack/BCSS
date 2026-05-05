from sqlalchemy import create_engine, text

engine = create_engine("postgresql://user:password@localhost:5432/BCSS")

with engine.connect() as conn:
    # TRUNCATE vacía la tabla y reinicia contadores de ID si los hay
    conn.execute(text("TRUNCATE TABLE star_match_planets RESTART IDENTITY;"))
    conn.commit()
    print("Tabla star_match_planets limpia.")