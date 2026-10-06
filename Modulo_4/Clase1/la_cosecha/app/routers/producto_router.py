from fastapi import APIRouter, HTTPException, status
from app.schemas.producto_schema import ProductoCrear, ProductoRespuesta
from app.services import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/", response_model=list[ProductoRespuesta])
def listar():
    return producto_service.listar_productos()


@router.post("/crear", response_model=ProductoRespuesta, status_code=status.HTTP_201_CREATED)
def crear(datos: ProductoCrear):
    return producto_service.crear_producto(datos)


@router.put("/actualizar/{producto_id}", response_model=ProductoRespuesta)
def actualizar(producto_id: int, datos: ProductoCrear):
    producto = producto_service.actualizar_producto(producto_id, datos)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/borrar/{producto_id}")
def eliminar(producto_id: int):
    eliminado = producto_service.eliminar_producto(producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": f"Producto {producto_id} eliminado correctamente"}