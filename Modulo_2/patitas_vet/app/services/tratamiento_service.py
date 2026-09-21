from sqlalchemy.orm import Session
from app.models.tratamiento_model import Tratamiento
from app.schemas.tratamiento_schemas import TratamientoCreate


def crear_tratamiento(db: Session, datos: TratamientoCreate):
    nuevo = Tratamiento(nombre=datos.nombre, precio=datos.precio)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_tratamientos(db: Session):
    return db.query(Tratamiento).all()


def obtener_tratamiento(db: Session, tratamiento_id: int):
    return db.query(Tratamiento).filter(Tratamiento.id == tratamiento_id).first()