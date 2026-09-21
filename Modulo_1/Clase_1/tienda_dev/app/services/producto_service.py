from sqlalchemy.orm import Session
from app.models.producto_model import Producto
from app.schemas.producto_schemas import ProductoCreate
from app.models.categoria_model import Categoria
from app.models.proveedor_model import Proveedor
from app.exceptions import CategoriaNoEncontrada, ProveedorNoEncontrado


def crear_producto(db: Session, datos: ProductoCreate):
    categoria = db.query(Categoria).filter(Categoria.id == datos.categoria_id).first()
    if categoria is None:
        raise CategoriaNoEncontrada(datos.categoria_id)

    if datos.proveedor_id is not None:
        proveedor = db.query(Proveedor).filter(Proveedor.id == datos.proveedor_id).first()
        if proveedor is None:
            raise ProveedorNoEncontrado(datos.proveedor_id)

    nuevo = Producto(
        nombre=datos.nombre,
        precio=datos.precio,
        stock=datos.stock,
        categoria_id=datos.categoria_id,
        proveedor_id=datos.proveedor_id,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def listar_productos(db: Session, categoria=None, precio_max=None):
    consulta = db.query(Producto)
    if categoria is not None:
        consulta = consulta.filter(Producto.categoria == categoria)
    if precio_max is not None:
        consulta = consulta.filter(Producto.precio <= precio_max)
    return consulta.all()


def obtener_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def actualizar_producto(db: Session, producto_id: int, datos: ProductoCreate):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto is None:
        return None

    categoria = db.query(Categoria).filter(Categoria.id == datos.categoria_id).first()
    if categoria is None:
        raise CategoriaNoEncontrada(datos.categoria_id)

    if datos.proveedor_id is not None:
        proveedor = db.query(Proveedor).filter(Proveedor.id == datos.proveedor_id).first()
        if proveedor is None:
            raise ProveedorNoEncontrado(datos.proveedor_id)

    producto.nombre = datos.nombre
    producto.precio = datos.precio
    producto.stock = datos.stock
    producto.categoria_id = datos.categoria_id
    producto.proveedor_id = datos.proveedor_id
    db.commit()
    db.refresh(producto)
    return producto


def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto is None:
        return False
    db.delete(producto)
    db.commit()
    return True

