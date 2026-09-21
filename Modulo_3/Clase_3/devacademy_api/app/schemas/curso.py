from pydantic import BaseModel

class CursoCreate(BaseModel):
    titulo: str
    descripcion: str

class CursoRespuesta(BaseModel):
    id: int
    titulo: str
    descripcion: str
    instructor_id: int

    class Config:
        from_attributes = True