from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    instructor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    instructor = relationship("Usuario", back_populates="cursos")
    lecciones = relationship("Leccion", back_populates="curso")