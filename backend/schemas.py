from pydantic import BaseModel, Field
from typing import Literal


class SerieCreate(BaseModel):
    titulo: str
    anio_estreno: int = Field(ge=1900, le=2030)
    temporadas: int = Field(ge=1, le=20)
    genero: str
    plataforma: str
    estado: Literal["En emisión", "Finalizada"]
    sinopsis: str
    imagen_url: str


class SerieUpdate(BaseModel):
    estado: Literal["En emisión", "Finalizada"]
    imagen_url: str
    temporadas: int = Field(ge=1, le=20)
