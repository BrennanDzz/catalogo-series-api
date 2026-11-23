from pydantic import BaseModel, Field
from typing import Literal


class SerieCreate(BaseModel):
    titulo: str
    anio_estreno: int = Field(ge=1900, le=2030)
    temporadas: int = Field(ge=1, le=10)
    genero: str
    plataforma: str
    estado: Literal["En emisión", "Finalizada"]
    sinopsis: str
    imagen_url: str


class SerieUpdate(BaseModel):
    titulo: str
    anio_estreno: int = Field(ge=1900, le=2030)
    temporadas: int = Field(ge=1, le=10)
    genero: str
    plataforma: str
    estado: Literal["En emisión", "Finalizada"]
    sinopsis: str
    imagen_url: str
