from pydantic import BaseModel, Field, field_validator


class ProveedorCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=80)
    email: str = Field(..., min_length=5)
    telefono: str | None = None

    @field_validator("email")
    @classmethod
    def validar_email(cls, valor: str) -> str:
        valor = valor.strip().lower()
        if "@" not in valor or "." not in valor:
            raise ValueError("El email no tiene un formato válido")
        return valor


class ProveedorRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str | None = None

    class Config:
        from_attributes = True