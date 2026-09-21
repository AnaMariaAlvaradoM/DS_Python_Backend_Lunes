from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services import consultas_service

router = APIRouter(tags=["Consultas"])


@router.get("/consultas/mascotas-con-dueno")
def mascotas_con_dueno(db: Session = Depends(get_db)):
    return consultas_service.mascotas_con_dueno(db)


@router.get("/consultas/citas-por-veterinario")
def citas_por_veterinario(db: Session = Depends(get_db)):
    return consultas_service.citas_por_veterinario(db)


@router.get("/consultas/insumos-por-agotarse")
def insumos_por_agotarse(minimo: int = 5, db: Session = Depends(get_db)):
    return consultas_service.insumos_por_agotarse(db, minimo)