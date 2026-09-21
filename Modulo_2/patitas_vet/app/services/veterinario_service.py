from sqlalchemy.orm import Session
from app.models.veterinario_model import Veterinario
from app.schemas.veterinario_schemas import VeterinarioCreate


def crear_veterinario(db: Session, datos: VeterinarioCreate):
    nuevo = Veterinario(nombre=datos.nombre, especialidad=datos.especialidad)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_veterinarios(db: Session):
    return db.query(Veterinario).all()


def obtener_veterinario(db: Session, veterinario_id: int):
    return db.query(Veterinario).filter(Veterinario.id == veterinario_id).first()