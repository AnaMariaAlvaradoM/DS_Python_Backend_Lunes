from pydantic import BaseModel, Field
from datetime import date


class MascotaCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=40)
    especie: str = Field(..., min_length=2, max_length=30)
    raza: str | None = None
    fecha_nacimiento: date | None = None
    dueno_id: int


class MascotaRespuesta(BaseModel):
    id: int
    nombre: str
    especie: str
    raza: str | None = None
    fecha_nacimiento: date | None = None
    dueno_id: int

    class Config:
        from_attributes = True