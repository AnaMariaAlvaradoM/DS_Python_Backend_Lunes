from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services import aplicacion_service

router = APIRouter(tags=["Aplicar Tratamiento"])


@router.post("/citas/{cita_id}/aplicar-tratamiento/{tratamiento_id}")
def aplicar(cita_id: int, tratamiento_id: int, db: Session = Depends(get_db)):
    return aplicacion_service.aplicar_tratamiento(db, tratamiento_id)