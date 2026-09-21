from sqlalchemy.orm import Session
from app.models.dueno_model import Dueno
from app.schemas.dueno_schemas import DuenoCreate


def crear_dueno(db: Session, datos: DuenoCreate):
    nuevo = Dueno(
        nombre=datos.nombre,
        telefono=datos.telefono,
        email=datos.email,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_duenos(db: Session):
    return db.query(Dueno).all()


def obtener_dueno(db: Session, dueno_id: int):
    return db.query(Dueno).filter(Dueno.id == dueno_id).first()


def actualizar_dueno(db: Session, dueno_id: int, datos: DuenoCreate):
    dueno = db.query(Dueno).filter(Dueno.id == dueno_id).first()
    if dueno is None:
        return None
    dueno.nombre = datos.nombre
    dueno.telefono = datos.telefono
    dueno.email = datos.email
    db.commit()
    db.refresh(dueno)
    return dueno


def eliminar_dueno(db: Session, dueno_id: int):
    dueno = db.query(Dueno).filter(Dueno.id == dueno_id).first()
    if dueno is None:
        return False
    db.delete(dueno)
    db.commit()
    return True