from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config.database import Base, SessionLocal, engine
from app.exceptions import CategoriaNoEncontrada, ProveedorNoEncontrado
from app.models import categoria_model, producto_model, proveedor_model
from app.routers import categoria_router, producto_router, proveedor_router
from app.services import categoria_services

Base.metadata.create_all(bind=engine)

# with SessionLocal() as db:
#     #categoria_services.inicializar_categorias_predeterminadas(db)

app = FastAPI(title="Tienda Dev API")

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
@app.exception_handler(CategoriaNoEncontrada)
def manejar_categoria_no_encontrada(request: Request, exc: CategoriaNoEncontrada):
    return JSONResponse(
        status_code=404,
        content={"error": "recurso_no_encontrado", "detalle": str(exc)},
    )


@app.exception_handler(ProveedorNoEncontrado)
def manejar_proveedor_no_encontrado(request: Request, exc: ProveedorNoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"error": "recurso_no_encontrado", "detalle": str(exc)},
    )


app.include_router(producto_router.router)
app.include_router(categoria_router.router)
app.include_router(proveedor_router.router)
