from sqlalchemy import Column, Integer, String
from app.config.database import Base


class Insumo(Base):
    __tablename__ = "insumos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    unidad = Column(String, nullable=True)