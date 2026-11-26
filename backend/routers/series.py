from fastapi import APIRouter, HTTPException, status
from schemas import SerieCreate, SerieUpdate
from services.series_services import consultar_todas_series, consultar_serie_id, crear_serie, editar_serie, eliminar_serie


router = APIRouter()


@router.get("/series")
def listar_series():
    return consultar_todas_series()


@router.get("/series/{id}")
def buscar_serie(id: int):
    serie = consultar_serie_id(id)

    if serie is None:
        raise HTTPException(
            status_code=404,
            detail="Serie no encontrada"
        )

    return serie


@router.post("/series", status_code=status.HTTP_201_CREATED)
def agregar_serie(serie: SerieCreate):
    return crear_serie(serie)


@router.put("/series/{id}")
def actualizar_serie(id: int, serie: SerieUpdate):
    serie_actualizada = editar_serie(id, serie)

    if serie_actualizada is None:
        raise HTTPException(
            status_code=404,
            detail="Serie no encontrada"
        )

    return serie_actualizada


@router.delete("/series/{id}", status_code=status.HTTP_204_NO_CONTENT)
def borrar_serie(id: int):
    serie_eliminada = eliminar_serie(id)

    if serie_eliminada is None:
        raise HTTPException(
            status_code=404,
            detail="Serie no encontrada"
        )

    return serie_eliminada
