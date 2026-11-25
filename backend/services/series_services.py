from database import conectar
from schemas import SerieCreate, SerieUpdate


def consultar_todas_series():
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM series ORDER BY id"
        ).fetchall()


def consultar_serie_id(id: int):
    with conectar() as conn:
        resultado = conn.execute(
            "SELECT * FROM series WHERE id = %s",
            (id,)
        )

        return resultado.fetchone()


def crear_serie(serie: SerieCreate):
    query = """
            INSERT INTO series (
                titulo,
                anio_estreno,
                temporadas,
                genero,
                plataforma,
                estado,
                sinopsis,
                imagen_url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *
        """

    parametros = (
        serie.titulo,
        serie.anio_estreno,
        serie.temporadas,
        serie.genero,
        serie.plataforma,
        serie.estado,
        serie.sinopsis,
        serie.imagen_url
    )

    with conectar() as conn:
        resultado = conn.execute(query, parametros)
        return resultado.fetchone()

    def editar_serie(id: int, serie: SerieUpdate):
    query = """
            UPDATE series
            SET estado = %s,
                imagen_url = %s
            WHERE id = %s
            RETURNING *
        """

    parametros = (serie.estado, serie.imagen_url, id)

    with conectar() as conn:
        resultado = conn.execute(query, parametros)
        return resultado.fetchone()
