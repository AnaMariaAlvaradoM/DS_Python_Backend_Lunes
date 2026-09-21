from pydantic import BaseModel
from datetime import date


class CitaCreate(BaseModel):
    fecha: date
    motivo: str
    mascota_id: int
    veterinario_id: int


class CitaRespuesta(BaseModel):
    id: int
    fecha: date
    motivo: str
    mascota_id: int
    veterinario_id: int

    class Config:
        from_attributes = True