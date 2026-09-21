from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_CONEXION = "postgresql+psycopg://postgres:admin@localhost:5432/patitas_vet"

engine = create_engine(URL_CONEXION)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()