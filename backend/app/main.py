"""
GNUVet API - Application Entry Point

Este é o ponto inicial da aplicação FastAPI.

Responsabilidades deste arquivo:
- Inicializar a aplicação FastAPI
- Configurar middlewares
- Registrar rotas
- Configurar logging
- Gerenciar ciclo de vida da aplicação (startup/shutdown)

IMPORTANTE:
Não colocar lógica de negócio aqui.
Toda regra deve ficar em:
services / domain / repository
"""

# ===============================
# IMPORTS
# ===============================

import logging
from contextlib import asynccontextmanager
import app.database.models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.session import engine

from app.routes import client_routes
from app.routes import pet_routes


# ===============================
# LOGGING CONFIGURATION
# ===============================

"""
Configuração básica de logging.

Em ambientes produtivos recomenda-se:
- JSON logs
- integração com ELK / Grafana / Datadog
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger("gnuvet")


# ===============================
# APPLICATION LIFECYCLE
# ===============================

"""
Lifespan substitui os antigos eventos:

@app.on_event("startup")
@app.on_event("shutdown")

Ele permite controlar o ciclo de vida da aplicação.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):

    # ==========================
    # STARTUP
    # ==========================

    logger.info("Starting GNUVet API...")

    # criação automática das tabelas
    # (em produção usar Alembic)
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized")

    yield

    # ==========================
    # SHUTDOWN
    # ==========================

    logger.info("Shutting down GNUVet API...")


# ===============================
# FASTAPI APPLICATION
# ===============================

app = FastAPI(
    title="GNUVet API",
    description="Veterinary clinic management system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


# ===============================
# CORS CONFIGURATION
# ===============================

"""
Permite acesso da API por aplicações frontend.

Em produção substituir "*" por domínios específicos.
"""

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===============================
# ROUTES REGISTRATION
# ===============================

"""
Registro de rotas da aplicação.

Cada módulo de rota deve possuir seu próprio router.
"""

app.include_router(client_routes.router)
app.include_router(pet_routes.router)

# ===============================
# HEALTH CHECK ENDPOINT
# ===============================

"""
Endpoint usado por:

- Docker
- Kubernetes
- Load balancers
- ferramentas de monitoramento
"""


@app.get("/health", tags=["Health"])
def health_check():

    return {
        "status": "running"
    }


# ===============================
# ROOT ENDPOINT
# ===============================

"""
Endpoint raiz da API.

Útil para:
- testes rápidos
- verificar se a API está online
"""


@app.get("/", tags=["Root"])
def root():

    return {
        "message": "GNUVet API running",
        "docs": "/docs",
    }