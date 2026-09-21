from sqlalchemy.orm import Session
from app.models.insumo_model import Insumo
from app.schemas.insumo_schemas import InsumoCreate


def crear_insumo(db: Session, datos: InsumoCreate):
    nuevo = Insumo(nombre=datos.nombre, stock=datos.stock, unidad=datos.unidad)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_insumos(db: Session):
    return db.query(Insumo).all()


def obtener_insumo(db: Session, insumo_id: int):
    return db.query(Insumo).filter(Insumo.id == insumo_id).first()