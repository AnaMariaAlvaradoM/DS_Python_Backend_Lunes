from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.cita_schemas import CitaCreate, CitaRespuesta
from app.services import cita_service

router = APIRouter(tags=["Citas"])


@router.post("/citas", response_model=CitaRespuesta)
def crear(datos: CitaCreate, db: Session = Depends(get_db)):
    return cita_service.crear_cita(db, datos)


@router.get("/citas", response_model=list[CitaRespuesta])
def listar(db: Session = Depends(get_db)):
    return cita_service.listar_citas(db)


@router.get("/citas/{cita_id}", response_model=CitaRespuesta)
def obtener(cita_id: int, db: Session = Depends(get_db)):
    cita = cita_service.obtener_cita(db, cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita