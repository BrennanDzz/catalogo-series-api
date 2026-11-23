from fastapi import APIRouter, HTTPException
from schemas import SerieCreate
from services.series_services import obtener_series, obtener_serie, agregar_serie


router = APIRouter()


@router.get("/series")
def listar_series():
    return obtener_series()
