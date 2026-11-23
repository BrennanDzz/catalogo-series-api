from fastapi import APIRouter, HTTPException
from schemas import SerieCreate
from services.series_services import obtener_series, obtener_serie, agregar_serie


router = APIRouter()


@router.get("/series")
def listar_series():
    return obtener_series()


@router.get("/series/{id}")
def detalle_serie(id: int):
    serie = obtener_serie(id)

    if serie is None:
        raise HTTPException(
            status_code=404,
            detail="Serie no encontrada"
        )

    return serie


@router.post("/series")
def crear_serie(serie: SerieCreate):
    return agregar_serie(serie)
