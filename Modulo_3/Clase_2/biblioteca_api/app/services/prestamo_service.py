from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.prestamo import Prestamo
from app.services.libro_service import obtener_libro

def crear_prestamo(db: Session, usuario_id: int, libro_id: int) -> Prestamo:
    libro = obtener_libro(db, libro_id)

    if libro.copias_disponibles < 1:
        raise HTTPException(status_code=400, detail="No hay copias disponibles")

    libro.copias_disponibles -= 1

    nuevo_prestamo = Prestamo(
        usuario_id=usuario_id,
        libro_id=libro_id,
        estado="activo"
    )
    db.add(nuevo_prestamo)
    db.commit()
    db.refresh(nuevo_prestamo)
    return nuevo_prestamo

def listar_prestamos_de_usuario(db: Session, usuario_id: int):
    return db.query(Prestamo).filter(Prestamo.usuario_id == usuario_id).all()

def devolver_prestamo(db: Session, prestamo_id: int, usuario_id: int) -> Prestamo:
    prestamo = db.query(Prestamo).filter(Prestamo.id == prestamo_id).first()
    if not prestamo:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    if prestamo.usuario_id != usuario_id:
        raise HTTPException(status_code=403, detail="Este préstamo no es tuyo")

    prestamo.estado = "devuelto"
    libro = obtener_libro(db, prestamo.libro_id)
    libro.copias_disponibles += 1
    db.commit()
    db.refresh(prestamo)
    return prestamo