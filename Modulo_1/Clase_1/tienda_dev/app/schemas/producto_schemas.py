from pydantic import BaseModel, Field, field_validator


class ProductoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    categoria_id: int
    proveedor_id: int | None = None

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, valor: str) -> str:
        valor_limpio = valor.strip()
        if valor_limpio == "":
            raise ValueError("El nombre no puede ser solo espacios")
        return valor_limpio

    # @field_validator("categoria")
    # @classmethod
    # def validar_categoria(cls, valor: str) -> str:
    #     categorias_validas = ["tecnologia", "papeleria", "hogar", "electronicos"]
    #     valor_limpio = valor.strip().lower()
    #     if valor_limpio not in categorias_validas:
    #         raise ValueError(f"Categoría inválida. Use una de: {categorias_validas}")
    #     return valor_limpio


class ProductoRespuesta(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria_id: int
    proveedor_id: int | None = None

class Config:
    from_attributes = True
