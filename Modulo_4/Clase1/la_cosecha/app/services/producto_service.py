from Modulo_4.Clase1.la_cosecha.app.schemas.producto_schema import ProductoCrear
from app.schemas.categoria_schema import CategoriaCrear

productos = []
contador_id = 1

def listar_productos():
    return productos;

def crear_productos(datos: ProductoCrear):
    global contador_id
    nuevo = {
        "id": contador_id,
        "nombre": datos.nombre,
        "precio": datos.precio,
        "stock": datos.stock,
        "categoria_id": datos.categoria_id
    }
    productos.append(nuevo)
    contador_id += 1
    return nuevo