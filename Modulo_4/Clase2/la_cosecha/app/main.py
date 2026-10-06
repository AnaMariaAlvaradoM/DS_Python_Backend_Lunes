from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app import models
from app.config.database import Base, engine
from app.routers import categoria_router, producto_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="API de La Cosecha", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categoria_router.router)
app.include_router(producto_router.router)

@app.get("/")
def raiz():
    return {"mensaje": "API de La Cosecha en línea 🌾"}