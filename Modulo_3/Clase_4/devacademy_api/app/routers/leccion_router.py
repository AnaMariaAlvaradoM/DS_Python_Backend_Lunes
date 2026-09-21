from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.leccion import LeccionCreate, LeccionRespuesta
from app.services.leccion_service import (
    crear_leccion,
    listar_lecciones_de_curso,
)
from app.auth.dependencias import (
    obtener_usuario_actual,
    requerir_instructor,
)
from app.models.usuario import Usuario

router = APIRouter(prefix="/lecciones", tags=["Lecciones"])

@router.post("/", response_model=LeccionRespuesta)
def post_leccion(
    datos: LeccionCreate,
    db: Session = Depends(get_db),
    instructor: Usuario = Depends(requerir_instructor)
):
    return crear_leccion(
        db,
        datos.titulo,
        datos.contenido,
        datos.curso_id,
        instructor.id
    )

@router.get(
    "/curso/{curso_id}",
    response_model=list[LeccionRespuesta]
)
def get_lecciones_de_curso(
    curso_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return listar_lecciones_de_curso(db, curso_id)