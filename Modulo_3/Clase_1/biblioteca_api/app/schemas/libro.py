from pydantic import BaseModel

class LibroCreate(BaseModel):
    titulo: str
    autor: str
    copias_disponibles: int = 1

class LibroRespuesta(BaseModel):
    id: int
    titulo: str
    autor: str
    copias_disponibles: int

    class Config:
        from_attributes = True