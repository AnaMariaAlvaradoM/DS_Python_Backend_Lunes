from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.libro import Libro
from app.schemas.libro import LibroCreate

def crear_libro(db: Session, datos: LibroCreate) -> Libro:
    nuevo_libro = Libro(
        titulo=datos.titulo,
        autor=datos.autor,
        copias_disponibles=datos.copias_disponibles
    )
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

def listar_libros(db: Session):
    return db.query(Libro).all()

def obtener_libro(db: Session, libro_id: int) -> Libro:
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro