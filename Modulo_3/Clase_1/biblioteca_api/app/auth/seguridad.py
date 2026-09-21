from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "clave-secreta-de-la-biblioteca-cambiar-en-produccion"
ALGORITHM = "HS256"
MINUTOS_EXPIRACION_TOKEN = 1

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashear_password(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(password_plano: str, password_hash: str) -> bool:
    return pwd_context.verify(password_plano, password_hash)

def crear_token(datos: dict) -> str:
    datos_a_codificar = datos.copy()
    expira = datetime.now(timezone.utc) + timedelta(minutes=MINUTOS_EXPIRACION_TOKEN)
    datos_a_codificar.update({"exp": expira})
    token = jwt.encode(datos_a_codificar, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None