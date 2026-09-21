from sqlalchemy import Column, Integer, String
from app.config.database import Base


class Dueno(Base):
    __tablename__ = "duenos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)