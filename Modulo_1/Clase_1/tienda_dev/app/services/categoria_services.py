from sqlalchemy.orm import Session

from app.models.categoria_model import Categoria
from app.schemas.categoria_schemas import CategoriaCreate


def crear_categoria(db: Session, datos: CategoriaCreate):
    nueva = Categoria(
        nombre=datos.nombre,
        descripcion=datos.descripcion,
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def listar_categorias(db: Session):
    return db.query(Categoria).all()


def obtener_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def actualizar_categoria(db: Session, categoria_id: int, datos: CategoriaCreate):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria is None:
        return None
    categoria.nombre = datos.nombre
    categoria.descripcion = datos.descripcion
    db.commit()
    db.refresh(categoria)
    return categoria


def eliminar_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria is None:
        return False
    db.delete(categoria)
    db.commit()
    return True
# def inicializar_categorias_predeterminadas(db: Session):
#     categorias_predeterminadas = [
#         ("Tecnología", "Productos tecnológicos"),
#         ("Papelería", "Útiles escolares y de oficina"),
#         ("Hogar", "Objetos para el hogar"),
#         ("Electrónicos", "Dispositivos electrónicos"),
#     ]

#     categorias_existentes = {
#         categoria.nombre.lower() for categoria in db.query(Categoria).all()
#     }

#     for nombre, descripcion in categorias_predeterminadas:
#         if nombre.lower() not in categorias_existentes:
#             db.add(Categoria(nombre=nombre, descripcion=descripcion))
#             categorias_existentes.add(nombre.lower())

#     db.commit()
