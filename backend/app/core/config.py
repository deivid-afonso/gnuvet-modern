"""
Arquivo responsável por centralizar
todas as configurações da aplicação.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # URL do banco de dados
    DATABASE_URL: str

    # chave usada para gerar JWT
    SECRET_KEY: str

    # algoritmo do token
    ALGORITHM: str = "HS256"

    # tempo de expiração do token
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


# instancia global
settings = Settings()