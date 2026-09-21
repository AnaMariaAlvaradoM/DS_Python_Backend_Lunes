from pydantic import BaseModel

class PrestamoCreate(BaseModel):
    libro_id: int

class PrestamoRespuesta(BaseModel):
    id: int
    usuario_id: int
    libro_id: int
    estado: str

    class Config:
        from_attributes = True