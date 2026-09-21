from pydantic import BaseModel, Field


class InsumoCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    stock: int = Field(..., ge=0)
    unidad: str | None = None


class InsumoRespuesta(BaseModel):
    id: int
    nombre: str
    stock: int
    unidad: str | None = None

    class Config:
        from_attributes = True