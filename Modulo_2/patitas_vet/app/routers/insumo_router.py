from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.insumo_schemas import InsumoCreate, InsumoRespuesta
from app.services import insumo_service

router = APIRouter(tags=["Insumos"])


@router.post("/insumos", response_model=InsumoRespuesta)
def crear(datos: InsumoCreate, db: Session = Depends(get_db)):
    return insumo_service.crear_insumo(db, datos)


@router.get("/insumos", response_model=list[InsumoRespuesta])
def listar(db: Session = Depends(get_db)):
    return insumo_service.listar_insumos(db)


@router.get("/insumos/{insumo_id}", response_model=InsumoRespuesta)
def obtener(insumo_id: int, db: Session = Depends(get_db)):
    insumo = insumo_service.obtener_insumo(db, insumo_id)
    if insumo is None:
        raise HTTPException(status_code=404, detail="Insumo no encontrado")
    return insumo