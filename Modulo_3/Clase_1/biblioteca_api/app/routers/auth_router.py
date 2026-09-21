from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.usuario import UsuarioCreate, UsuarioRespuesta
from app.services.usuario_service import registrar_usuario
from app.models.usuario import Usuario
from app.auth.seguridad import verificar_password, crear_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/registro", response_model=UsuarioRespuesta)
def registro(datos: UsuarioCreate, db: Session = Depends(get_db)):
    return registrar_usuario(db, datos)

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")

    token = crear_token({"sub": str(usuario.id)})
    return {"access_token": token, "token_type": "bearer"}