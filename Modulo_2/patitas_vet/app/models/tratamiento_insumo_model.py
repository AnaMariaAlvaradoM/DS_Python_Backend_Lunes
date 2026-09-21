from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class TratamientoInsumo(Base):
    __tablename__ = "tratamiento_insumo"

    id = Column(Integer, primary_key=True, index=True)
    tratamiento_id = Column(Integer, ForeignKey("tratamientos.id"), nullable=False)
    insumo_id = Column(Integer, ForeignKey("insumos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)

    insumo = relationship("Insumo")