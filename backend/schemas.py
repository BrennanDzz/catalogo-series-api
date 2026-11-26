from pydantic import BaseModel, Field, StringConstraints
from typing import Annotated, Literal


class SerieCreate(BaseModel):
    titulo: Annotated[str, StringConstraints(
        strip_whitespace=True, min_length=1, max_length=100)]
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
