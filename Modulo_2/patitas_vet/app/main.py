from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config.database import Base, engine
from app.models import dueno_model, mascota_model, veterinario_model, cita_model, tratamiento_model, tratamiento_insumo_model, insumo_model
from app.routers import dueno_router, mascota_router, veterinario_router, cita_router, tratamiento_router, tratamiento_insumo_router, insumo_router, aplicacion_router, consultas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patitas Vet API")

app.include_router(dueno_router.router)
app.include_router(mascota_router.router)
app.include_router(veterinario_router.router)
app.include_router(cita_router.router)
app.include_router(insumo_router.router)
app.include_router(tratamiento_router.router)
app.include_router(tratamiento_insumo_router.router)
app.include_router(aplicacion_router.router)
app.include_router(consultas_router.router)

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"


@app.get("/", response_class=HTMLResponse)
def index():
    index_path = TEMPLATES_DIR / "index.html"
    return HTMLResponse(index_path.read_text(encoding="utf-8"))