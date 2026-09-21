from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.cita_model import Cita
from app.models.mascota_model import Mascota
from app.models.veterinario_model import Veterinario
from app.schemas.cita_schemas import CitaCreate


def crear_cita(db: Session, datos: CitaCreate):
    mascota = db.query(Mascota).filter(Mascota.id == datos.mascota_id).first()
    if mascota is None:
        raise HTTPException(status_code=404, detail="La mascota indicada no existe")

    veterinario = db.query(Veterinario).filter(Veterinario.id == datos.veterinario_id).first()
    if veterinario is None:
        raise HTTPException(status_code=404, detail="El veterinario indicado no existe")

    nueva = Cita(
        fecha=datos.fecha,
        motivo=datos.motivo,
        mascota_id=datos.mascota_id,
        veterinario_id=datos.veterinario_id,
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_citas(db: Session):
    return db.query(Cita).all()


def obtener_cita(db: Session, cita_id: int):
    return db.query(Cita).filter(Cita.id == cita_id).first()