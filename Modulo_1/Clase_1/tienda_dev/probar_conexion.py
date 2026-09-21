from sqlalchemy import text
from app.config.database import engine

with engine.connect() as conexion:
    resultado = conexion.execute(text("SELECT version();"))
    print("✅ Conexión exitosa:")
    print(resultado.fetchone()[0])  