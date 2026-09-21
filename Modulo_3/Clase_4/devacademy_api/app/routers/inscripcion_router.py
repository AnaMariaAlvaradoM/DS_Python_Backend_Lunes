from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.inscripcion import (
    InscripcionCreate,
    InscripcionRespuesta,
)
from app.services.inscripcion_service import (
    inscribir,
    listar_mis_inscripciones,
)
from app.auth.dependencias import obtener_usuario_actual
from app.models.usuario import Usuario

router = APIRouter(
    prefix="/inscripciones",
    tags=["Inscripciones"]
)

@router.post("/", response_model=InscripcionRespuesta)
def post_inscripcion(
    datos: InscripcionCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return inscribir(db, usuario.id, datos.curso_id)

@router.get(
    "/mis-inscripciones",
    response_model=list[InscripcionRespuesta]
)
def get_mis_inscripciones(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return listar_mis_inscripciones(db, usuario.id)