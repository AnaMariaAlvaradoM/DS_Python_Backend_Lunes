from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.tratamiento_insumo_schemas import RecetaItemCreate, RecetaItemRespuesta
from app.services import tratamiento_insumo_service

router = APIRouter(tags=["Recetas"])


@router.post("/tratamientos/{tratamiento_id}/insumos", response_model=RecetaItemRespuesta)
def agregar_insumo(tratamiento_id: int, datos: RecetaItemCreate, db: Session = Depends(get_db)):
    return tratamiento_insumo_service.agregar_insumo_a_receta(db, tratamiento_id, datos)


@router.get("/tratamientos/{tratamiento_id}/insumos", response_model=list[RecetaItemRespuesta])
def ver_receta(tratamiento_id: int, db: Session = Depends(get_db)):
    return tratamiento_insumo_service.ver_receta(db, tratamiento_id)