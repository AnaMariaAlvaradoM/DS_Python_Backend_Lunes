from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.categoria_schemas import CategoriaCreate, CategoriaRespuesta
from app.services import categoria_services

router = APIRouter()


@router.post("/categorias", response_model=CategoriaRespuesta)
def crear(datos: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_services.crear_categoria(db, datos)


@router.get("/categorias", response_model=list[CategoriaRespuesta])
def listar(db: Session = Depends(get_db)):
    return categoria_services.listar_categorias(db)


@router.get("/categorias/{categoria_id}", response_model=CategoriaRespuesta)
def obtener(categoria_id: int, db: Session = Depends(get_db)):
    return categoria_services.obtener_categoria(db, categoria_id)


@router.put("/categorias/{categoria_id}", response_model=CategoriaRespuesta)
def actualizar(categoria_id: int, datos: CategoriaCreate, db: Session = Depends(get_db)):
    categoria = categoria_services.actualizar_categoria(db, categoria_id, datos)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.delete("/categorias/{categoria_id}")
def eliminar(categoria_id: int, db: Session = Depends(get_db)):
    eliminado = categoria_services.eliminar_categoria(db, categoria_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"mensaje": f"Categoría {categoria_id} eliminada"}