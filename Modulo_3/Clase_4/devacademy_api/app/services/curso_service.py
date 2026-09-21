from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.curso import Curso

def crear_curso(
    db: Session,
    titulo: str,
    descripcion: str,
    instructor_id: int
) -> Curso:
    nuevo_curso = Curso(
        titulo=titulo,
        descripcion=descripcion,
        instructor_id=instructor_id
    )
    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)
    return nuevo_curso

def listar_cursos(db: Session):
    return db.query(Curso).all()

def obtener_curso(db: Session, curso_id: int) -> Curso:
    curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    return curso


def actualizar_curso(
    db: Session,
    curso_id: int,
    titulo: str,
    descripcion: str,
    instructor_id: int,
    rol: str
) -> Curso:
    curso = obtener_curso(db, curso_id)
    if curso.instructor_id != instructor_id and rol != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Este curso no es tuyo"
    )
    curso.titulo = titulo
    curso.descripcion = descripcion
    db.commit()
    db.refresh(curso)
    return curso