from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.libro import LibroCreate, LibroRespuesta
from app.services.libro_service import crear_libro, listar_libros, obtener_libro
from app.auth.dependencias import requerir_admin
from app.models.usuario import Usuario

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/", response_model=list[LibroRespuesta])
def get_libros(db: Session = Depends(get_db)):
    return listar_libros(db)

@router.get("/{libro_id}", response_model=LibroRespuesta)
def get_libro(libro_id: int, db: Session = Depends(get_db)):
    return obtener_libro(db, libro_id)

@router.post("/", response_model=LibroRespuesta)
def post_libro(
    datos: LibroCreate,
    db: Session = Depends(get_db),
    admin: Usuario = Depends(requerir_admin)
):
    return crear_libro(db, datos)