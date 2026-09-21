from pydantic import BaseModel, Field, EmailStr, field_validator


class DuenoCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=60)
    telefono: str = Field(..., min_length=7, max_length=15)
    email: EmailStr

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, valor: str) -> str:
        limpio = valor.strip()
        if limpio == "":
            raise ValueError("El nombre no puede estar vacío")
        return limpio


class DuenoRespuesta(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str

    class Config:
        from_attributes = True