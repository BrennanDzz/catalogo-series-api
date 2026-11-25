from fastapi import APIRouter, HTTPException
from schemas import SerieCreate
from services.series_services import consultar_todas_series, consultar_serie_id, crear_serie


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


@router.post("/series")
def agregar_serie(serie: SerieCreate):
    return crear_serie(serie)