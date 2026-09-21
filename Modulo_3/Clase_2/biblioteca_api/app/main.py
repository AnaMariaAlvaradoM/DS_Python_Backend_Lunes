from fastapi import FastAPI
from app.database import Base, engine

from app.models import usuario, libro, prestamo

from app.routers import auth_router, usuario_router, libro_router, prestamo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Biblioteca API", description="API con autenticación JWT")

app.include_router(auth_router.router)
app.include_router(usuario_router.router)
app.include_router(libro_router.router)
app.include_router(prestamo_router.router)

@app.get("/")
def raiz():
    return {"mensaje": "API de Biblioteca funcionando"}