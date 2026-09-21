from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.prestamo import PrestamoCreate, PrestamoRespuesta
from app.services.prestamo_service import (
    crear_prestamo,
    listar_prestamos_de_usuario,
    devolver_prestamo,
)
from app.auth.dependencias import obtener_usuario_actual
from app.models.usuario import Usuario

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=PrestamoRespuesta)
def post_prestamo(
    datos: PrestamoCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return crear_prestamo(db, usuario.id, datos.libro_id)

@router.get("/mis-prestamos", response_model=list[PrestamoRespuesta])
def get_mis_prestamos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return listar_prestamos_de_usuario(db, usuario.id)

@router.put("/{prestamo_id}/devolver", response_model=PrestamoRespuesta)
def put_devolver(
    prestamo_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return devolver_prestamo(db, prestamo_id, usuario.id)