from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.veterinario_schemas import VeterinarioCreate, VeterinarioRespuesta
from app.services import veterinario_service

router = APIRouter(tags=["Veterinarios"])


@router.post("/veterinarios", response_model=VeterinarioRespuesta)
def crear(datos: VeterinarioCreate, db: Session = Depends(get_db)):
    return veterinario_service.crear_veterinario(db, datos)


@router.get("/veterinarios", response_model=list[VeterinarioRespuesta])
def listar(db: Session = Depends(get_db)):
    return veterinario_service.listar_veterinarios(db)


@router.get("/veterinarios/{veterinario_id}", response_model=VeterinarioRespuesta)
def obtener(veterinario_id: int, db: Session = Depends(get_db)):
    veterinario = veterinario_service.obtener_veterinario(db, veterinario_id)
    if veterinario is None:
        raise HTTPException(status_code=404, detail="Veterinario no encontrado")
    return veterinario