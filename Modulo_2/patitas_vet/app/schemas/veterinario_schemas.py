from pydantic import BaseModel, Field


class VeterinarioCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=60)
    especialidad: str = Field(..., min_length=2, max_length=40)


class VeterinarioRespuesta(BaseModel):
    id: int
    nombre: str
    especialidad: str

    class Config:
        from_attributes = True