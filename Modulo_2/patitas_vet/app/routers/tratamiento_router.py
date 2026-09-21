from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.tratamiento_schemas import TratamientoCreate, TratamientoRespuesta
from app.services import tratamiento_service

router = APIRouter(tags=["Tratamientos"])


@router.post("/tratamientos", response_model=TratamientoRespuesta)
def crear(datos: TratamientoCreate, db: Session = Depends(get_db)):
    return tratamiento_service.crear_tratamiento(db, datos)


@router.get("/tratamientos", response_model=list[TratamientoRespuesta])
def listar(db: Session = Depends(get_db)):
    return tratamiento_service.listar_tratamientos(db)


@router.get("/tratamientos/{tratamiento_id}", response_model=TratamientoRespuesta)
def obtener(tratamiento_id: int, db: Session = Depends(get_db)):
    tratamiento = tratamiento_service.obtener_tratamiento(db, tratamiento_id)
    if tratamiento is None:
        raise HTTPException(status_code=404, detail="Tratamiento no encontrado")
    return tratamiento