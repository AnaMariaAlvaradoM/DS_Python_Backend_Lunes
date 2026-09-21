from pydantic import BaseModel

class LeccionCreate(BaseModel):
    titulo: str
    contenido: str
    curso_id: int

class LeccionRespuesta(BaseModel):
    id: int
    titulo: str
    contenido: str
    curso_id: int

    class Config:
        from_attributes = True