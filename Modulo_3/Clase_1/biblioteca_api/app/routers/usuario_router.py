from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario import UsuarioRespuesta
from app.services.usuario_service import listar_usuarios, obtener_usuario, eliminar_usuario
from app.auth.dependencias import requerir_admin
from app.models.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=list[UsuarioRespuesta])
def get_usuarios(
    db: Session = Depends(get_db),
    admin: Usuario = Depends(requerir_admin)
):
    return listar_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioRespuesta)
def get_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(requerir_admin)
):
    return obtener_usuario(db, usuario_id)

@router.delete("/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(requerir_admin)
):
    return eliminar_usuario(db, usuario_id)