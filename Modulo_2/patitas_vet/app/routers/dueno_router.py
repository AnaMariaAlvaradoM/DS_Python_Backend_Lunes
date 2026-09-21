from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.dueno_schemas import DuenoCreate, DuenoRespuesta
from app.services import dueno_service

router = APIRouter(tags=["Dueños"])


@router.post("/duenos", response_model=DuenoRespuesta)
def crear(datos: DuenoCreate, db: Session = Depends(get_db)):
    return dueno_service.crear_dueno(db, datos)


@router.get("/duenos", response_model=list[DuenoRespuesta])
def listar(db: Session = Depends(get_db)):
    return dueno_service.listar_duenos(db)


@router.get("/duenos/{dueno_id}", response_model=DuenoRespuesta)
def obtener(dueno_id: int, db: Session = Depends(get_db)):
    dueno = dueno_service.obtener_dueno(db, dueno_id)
    if dueno is None:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return dueno


@router.put("/duenos/{dueno_id}", response_model=DuenoRespuesta)
def actualizar(dueno_id: int, datos: DuenoCreate, db: Session = Depends(get_db)):
    dueno = dueno_service.actualizar_dueno(db, dueno_id, datos)
    if dueno is None:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return dueno


@router.delete("/duenos/{dueno_id}")
def eliminar(dueno_id: int, db: Session = Depends(get_db)):
    eliminado = dueno_service.eliminar_dueno(db, dueno_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Dueño no encontrado")
    return {"mensaje": f"Dueño {dueno_id} eliminado"}