from pydantic import BaseModel

class InscripcionCreate(BaseModel):
    curso_id: int

class InscripcionRespuesta(BaseModel):
    id: int
    estudiante_id: int
    curso_id: int
    estado: str

    class Config:
        from_attributes = True