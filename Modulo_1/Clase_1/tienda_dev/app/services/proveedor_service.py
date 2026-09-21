from sqlalchemy.orm import Session

from app.models.proveedor_model import Proveedor
from app.schemas.proveedor_schemas import ProveedorCreate


def crear_proveedor(db: Session, datos: ProveedorCreate):
    nuevo = Proveedor(
        nombre=datos.nombre,
        email=datos.email,
        telefono=datos.telefono,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_proveedores(db: Session):
    return db.query(Proveedor).all()


def obtener_proveedor(db: Session, proveedor_id: int):
    return db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()


def actualizar_proveedor(db: Session, proveedor_id: int, datos: ProveedorCreate):
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if proveedor is None:
        return None
    proveedor.nombre = datos.nombre
    proveedor.email = datos.email
    proveedor.telefono = datos.telefono
    db.commit()
    db.refresh(proveedor)
    return proveedor


def eliminar_proveedor(db: Session, proveedor_id: int):
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if proveedor is None:
        return False
    db.delete(proveedor)
    db.commit()
    return True