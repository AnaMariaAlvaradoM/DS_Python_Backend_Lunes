from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas.producto_schemas import ProductoCreate, ProductoRespuesta
from app.services import producto_service

router = APIRouter()


@router.post("/productos", response_model=ProductoRespuesta)
def crear(datos: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.crear_producto(db, datos)


@router.get("/productos", response_model=list[ProductoRespuesta])
def listar(categoria: str | None = None, precio_max: float | None = None,
           db: Session = Depends(get_db)):
    return producto_service.listar_productos(db, categoria, precio_max)


@router.get("/productos/{producto_id}", response_model=ProductoRespuesta)
def obtener(producto_id: int, db: Session = Depends(get_db)):
    return producto_service.obtener_producto(db, producto_id)


@router.put("/productos/{producto_id}", response_model=ProductoRespuesta)
def actualizar(producto_id: int, datos: ProductoCreate, db: Session = Depends(get_db)):
    producto = producto_service.actualizar_producto(db, producto_id, datos)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/productos/{producto_id}")
def eliminar(producto_id: int, db: Session = Depends(get_db)):
    eliminado = producto_service.eliminar_producto(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto {producto_id} eliminado"}