from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.mascota_model import Mascota
from app.models.dueno_model import Dueno
from app.schemas.mascota_schemas import MascotaCreate


def crear_mascota(db: Session, datos: MascotaCreate):
    dueno = db.query(Dueno).filter(Dueno.id == datos.dueno_id).first()
    if dueno is None:
        raise HTTPException(status_code=404, detail="El dueño indicado no existe")

    nueva = Mascota(
        nombre=datos.nombre,
        especie=datos.especie,
        raza=datos.raza,
        fecha_nacimiento=datos.fecha_nacimiento,
        dueno_id=datos.dueno_id,
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_mascotas(db: Session, dueno_id=None):
    consulta = db.query(Mascota)
    if dueno_id is not None:
        consulta = consulta.filter(Mascota.dueno_id == dueno_id)
    return consulta.all()


def obtener_mascota(db: Session, mascota_id: int):
    return db.query(Mascota).filter(Mascota.id == mascota_id).first()


def eliminar_mascota(db: Session, mascota_id: int):
    mascota = db.query(Mascota).filter(Mascota.id == mascota_id).first()
    if mascota is None:
        return False
    db.delete(mascota)
    db.commit()
    return True