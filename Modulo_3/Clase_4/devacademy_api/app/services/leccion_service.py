from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.leccion import Leccion
from app.services.curso_service import obtener_curso

def crear_leccion(
    db: Session,
    titulo: str,
    contenido: str,
    curso_id: int,
    usuario_id: int
) -> Leccion:
    curso = obtener_curso(db, curso_id)

    if curso.instructor_id != usuario_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No puedes agregar lecciones a un curso que no es tuyo"
        )

    nueva_leccion = Leccion(
        titulo=titulo,
        contenido=contenido,
        curso_id=curso_id
    )
    db.add(nueva_leccion)
    db.commit()
    db.refresh(nueva_leccion)
    return nueva_leccion

def listar_lecciones_de_curso(db: Session, curso_id: int):
    obtener_curso(db, curso_id)
    return db.query(Leccion).filter(
        Leccion.curso_id == curso_id
    ).all()