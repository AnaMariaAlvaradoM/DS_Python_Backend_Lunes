from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.inscripcion import Inscripcion
from app.services.curso_service import obtener_curso

def inscribir(
    db: Session,
    estudiante_id: int,
    curso_id: int
) -> Inscripcion:
    obtener_curso(db, curso_id)

    existente = db.query(Inscripcion).filter(
        Inscripcion.estudiante_id == estudiante_id,
        Inscripcion.curso_id == curso_id
    ).first()
    if existente:
        raise HTTPException(
            status_code=400,
            detail="Ya estás inscrito en este curso"
        )

    nueva = Inscripcion(
        estudiante_id=estudiante_id,
        curso_id=curso_id,
        estado="activa"
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_mis_inscripciones(db: Session, estudiante_id: int):
    return db.query(Inscripcion).filter(
        Inscripcion.estudiante_id == estudiante_id
    ).all()