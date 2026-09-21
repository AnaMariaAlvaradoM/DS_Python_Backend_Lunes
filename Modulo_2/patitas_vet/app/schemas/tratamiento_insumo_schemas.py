from pydantic import BaseModel, Field


class RecetaItemCreate(BaseModel):
    insumo_id: int
    cantidad: int = Field(..., gt=0)


class RecetaItemRespuesta(BaseModel):
    id: int
    tratamiento_id: int
    insumo_id: int
    cantidad: int

    class Config:
        from_attributes = True