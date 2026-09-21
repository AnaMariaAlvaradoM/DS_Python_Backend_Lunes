from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.tratamiento_insumo_model import TratamientoInsumo
from app.models.tratamiento_model import Tratamiento
from app.models.insumo_model import Insumo
from app.schemas.tratamiento_insumo_schemas import RecetaItemCreate


def agregar_insumo_a_receta(db: Session, tratamiento_id: int, datos: RecetaItemCreate):
    tratamiento = db.query(Tratamiento).filter(Tratamiento.id == tratamiento_id).first()
    if tratamiento is None:
        raise HTTPException(status_code=404, detail="El tratamiento no existe")

    insumo = db.query(Insumo).filter(Insumo.id == datos.insumo_id).first()
    if insumo is None:
        raise HTTPException(status_code=404, detail="El insumo no existe")

    linea = TratamientoInsumo(
        tratamiento_id=tratamiento_id,
        insumo_id=datos.insumo_id,
        cantidad=datos.cantidad,
    )
    db.add(linea)
    db.commit()
    db.refresh(linea)
    return linea


def ver_receta(db: Session, tratamiento_id: int):
    return db.query(TratamientoInsumo).filter(
        TratamientoInsumo.tratamiento_id == tratamiento_id
    ).all()