from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.curso import CursoCreate, CursoRespuesta
from app.services.curso_service import (
    crear_curso,
    listar_cursos,
    obtener_curso,
    actualizar_curso,
)
from app.auth.dependencias import requerir_instructor
from app.models.usuario import Usuario

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.get("/", response_model=list[CursoRespuesta])
def get_cursos(db: Session = Depends(get_db)):
    return listar_cursos(db)

@router.get("/{curso_id}", response_model=CursoRespuesta)
def get_curso(curso_id: int, db: Session = Depends(get_db)):
    return obtener_curso(db, curso_id)

@router.post("/", response_model=CursoRespuesta)
def post_curso(
    datos: CursoCreate,
    db: Session = Depends(get_db),
    instructor: Usuario = Depends(requerir_instructor)
):
    return crear_curso(
        db,
        datos.titulo,
        datos.descripcion,
        instructor.id
    )

@router.put("/{curso_id}", response_model=CursoRespuesta)
def put_curso(
    curso_id: int,
    datos: CursoCreate,
    db: Session = Depends(get_db),
    instructor: Usuario = Depends(requerir_instructor)
):
    return actualizar_curso(
        db,
        curso_id,
        datos.titulo,
        datos.descripcion,
        instructor.id,
        rol= instructor.rol
    )