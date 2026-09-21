from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.tratamiento_model import Tratamiento
from app.models.tratamiento_insumo_model import TratamientoInsumo
from app.models.insumo_model import Insumo


def aplicar_tratamiento(db: Session, tratamiento_id: int):
    tratamiento = db.query(Tratamiento).filter(Tratamiento.id == tratamiento_id).first()
    if tratamiento is None:
        raise HTTPException(status_code=404, detail="El tratamiento no existe")

    receta = db.query(TratamientoInsumo).filter(
        TratamientoInsumo.tratamiento_id == tratamiento_id
    ).all()

    if not receta:
        raise HTTPException(status_code=400, detail="El tratamiento no tiene receta definida")

    # PASO 1: verificar que haya stock de TODOS antes de tocar nada
    for linea in receta:
        insumo = db.query(Insumo).filter(Insumo.id == linea.insumo_id).first()
        if insumo.stock < linea.cantidad:
            raise HTTPException(
                status_code=409,
                detail=f"Stock insuficiente de {insumo.nombre}: hay {insumo.stock}, se necesitan {linea.cantidad}",
            )

    # PASO 2: si llegamos aquí, TODO alcanza. Ahora sí descontamos.
    for linea in receta:
        insumo = db.query(Insumo).filter(Insumo.id == linea.insumo_id).first()
        insumo.stock = insumo.stock - linea.cantidad

    db.commit()
    return {"mensaje": f"Tratamiento '{tratamiento.nombre}' aplicado. Inventario actualizado."}