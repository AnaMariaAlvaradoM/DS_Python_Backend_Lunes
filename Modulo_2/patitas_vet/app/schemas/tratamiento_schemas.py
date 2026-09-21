from pydantic import BaseModel, Field


class TratamientoCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    precio: float = Field(..., gt=0)


class TratamientoRespuesta(BaseModel):
    id: int
    nombre: str
    precio: float

    class Config:
        from_attributes = True