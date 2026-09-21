from sqlalchemy.orm import Session
from app.models.mascota_model import Mascota
from app.models.dueno_model import Dueno

from sqlalchemy import func
from app.models.cita_model import Cita
from app.models.veterinario_model import Veterinario


from app.models.insumo_model import Insumo


def insumos_por_agotarse(db: Session, minimo: int = 5):
    return db.query(Insumo).filter(Insumo.stock < minimo).all()

def citas_por_veterinario(db: Session):
    resultado = (
        db.query(Veterinario.nombre, func.count(Cita.id).label("total_citas"))
        .join(Cita, Cita.veterinario_id == Veterinario.id)
        .group_by(Veterinario.nombre)
        .all()
    )
    return [{"veterinario": fila.nombre, "total_citas": fila.total_citas} for fila in resultado]

def mascotas_con_dueno(db: Session):
    resultado = (
        db.query(Mascota.nombre, Dueno.nombre.label("dueno"))
        .join(Dueno, Mascota.dueno_id == Dueno.id)
        .all()
    )
    return [{"mascota": fila.nombre, "dueno": fila.dueno} for fila in resultado]