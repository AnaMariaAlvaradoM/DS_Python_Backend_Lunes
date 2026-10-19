from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    admin_nombre: str
    admin_correo: str
    admin_contrasena: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
