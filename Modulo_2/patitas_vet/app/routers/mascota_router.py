from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.mascota_schemas import MascotaCreate, MascotaRespuesta
from app.services import mascota_service

router = APIRouter(tags=["Mascotas"])


@router.post("/mascotas", response_model=MascotaRespuesta)
def crear(datos: MascotaCreate, db: Session = Depends(get_db)):
    return mascota_service.crear_mascota(db, datos)


@router.get("/mascotas", response_model=list[MascotaRespuesta])
def listar(dueno_id: int | None = None, db: Session = Depends(get_db)):
    return mascota_service.listar_mascotas(db, dueno_id)


@router.get("/mascotas/{mascota_id}", response_model=MascotaRespuesta)
def obtener(mascota_id: int, db: Session = Depends(get_db)):
    mascota = mascota_service.obtener_mascota(db, mascota_id)
    if mascota is None:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return mascota


@router.delete("/mascotas/{mascota_id}")
def eliminar(mascota_id: int, db: Session = Depends(get_db)):
    eliminado = mascota_service.eliminar_mascota(db, mascota_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")
    return {"mensaje": f"Mascota {mascota_id} eliminada"}