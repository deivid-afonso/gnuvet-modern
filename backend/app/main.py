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
from app.routes import appointment_routes


# ===============================
# LOGGING CONFIGURATION
# ===============================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger("gnuvet")


# ===============================
# APPLICATION LIFECYCLE
# ===============================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Starting GNUVet API...")

    # cria tabelas automaticamente
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized")

    yield

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

app.include_router(client_routes.router)
app.include_router(pet_routes.router)
app.include_router(appointment_routes.router)


# ===============================
# HEALTH CHECK ENDPOINT
# ===============================

@app.get("/health", tags=["Health"])
def health_check():

    return {"status": "running"}


# ===============================
# ROOT ENDPOINT
# ===============================

@app.get("/", tags=["Root"])
def root():

    return {
        "message": "GNUVet API running",
        "docs": "/docs",
    }