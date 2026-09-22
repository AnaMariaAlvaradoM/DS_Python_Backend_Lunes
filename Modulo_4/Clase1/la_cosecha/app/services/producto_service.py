from app.schemas.producto_schema import ProductoCrear

productos = []
contador_id = 1

def listar_productos():
    return productos;


def crear_producto(datos: ProductoCrear):
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

def buscar_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    return None

def actualizar_producto(producto_id: int, datos: ProductoCrear):
    producto = buscar_producto(producto_id)
    if producto is None:
        return None
    producto["nombre"] = datos.nombre
    producto["precio"] = datos.precio
    producto["stock"] = datos.stock
    producto["categoria_id"] = datos.categoria_id

    return producto 

def eliminar_producto(producto_id: int):
    producto = buscar_producto(producto_id)
    if producto:
        return True


