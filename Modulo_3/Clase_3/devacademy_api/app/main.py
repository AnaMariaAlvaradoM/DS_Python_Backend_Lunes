from fastapi import FastAPI
from app.database import Base, engine

from app.models import usuario, curso, leccion, inscripcion

from app.routers import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevAcademy API", description="Backend de la plataforma DevAcademy")

app.include_router(auth_router.router)

@app.get("/")
def raiz():
    return {"mensaje": "DevAcademy API funcionando"}