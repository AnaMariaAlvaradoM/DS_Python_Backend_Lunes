from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.proveedor_schemas import ProveedorCreate, ProveedorRespuesta
from app.services import proveedor_service

router = APIRouter()


@router.post("/proveedores", response_model=ProveedorRespuesta)
def crear(datos: ProveedorCreate, db: Session = Depends(get_db)):
    return proveedor_service.crear_proveedor(db, datos)


@router.get("/proveedores", response_model=list[ProveedorRespuesta])
def listar(db: Session = Depends(get_db)):
    return proveedor_service.listar_proveedores(db)


@router.get("/proveedores/{proveedor_id}", response_model=ProveedorRespuesta)
def obtener(proveedor_id: int, db: Session = Depends(get_db)):
    return proveedor_service.obtener_proveedor(db, proveedor_id)


from fastapi import HTTPException


@router.put("/proveedores/{proveedor_id}", response_model=ProveedorRespuesta)
def actualizar(proveedor_id: int, datos: ProveedorCreate, db: Session = Depends(get_db)):
    proveedor = proveedor_service.actualizar_proveedor(db, proveedor_id, datos)
    if proveedor is None:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor


@router.delete("/proveedores/{proveedor_id}")
def eliminar(proveedor_id: int, db: Session = Depends(get_db)):
    eliminado = proveedor_service.eliminar_proveedor(db, proveedor_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return {"mensaje": f"Proveedor {proveedor_id} eliminado"}