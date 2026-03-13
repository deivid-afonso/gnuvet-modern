"""
Cria a conexão com o banco de dados.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


# engine cria conexão com banco
engine = create_engine(settings.DATABASE_URL)

# sessão do SQLAlchemy
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    Dependency do FastAPI para
    abrir e fechar sessão automaticamente
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()