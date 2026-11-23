from database import conectar
from schemas import SerieCreate


def obtener_series():
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM series ORDER BY id"
        ).fetchall()


def obtener_serie(id: int):
    with conectar() as conn:
        resultado = conn.execute(
            "SELECT * FROM series WHERE id = %s",
            (id,)
        )

        return resultado.fetchone()
