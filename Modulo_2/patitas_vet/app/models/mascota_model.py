from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class Mascota(Base):
    __tablename__ = "mascotas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    raza = Column(String, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)

    dueno_id = Column(Integer, ForeignKey("duenos.id"), nullable=False)

    dueno = relationship("Dueno")