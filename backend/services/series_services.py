from database import conectar
from schemas import SerieCreate


def obtener_series():
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM series ORDER BY id"
        ).fetchall()
