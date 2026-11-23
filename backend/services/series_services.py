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

    def agregar_serie(serie: SerieCreate):
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
