"""
Endpoints da API para Client.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.services.client_service import ClientService
from app.schemas.client_schema import (
    ClientCreate,
    ClientResponse
)

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@router.get(
    "/",
    response_model=List[ClientResponse]
)
def list_clients(
    db: Session = Depends(get_db)
):
    """
    Lista todos os clientes.
    """

    service = ClientService(db)

    return service.list_clients()


@router.post(
    "/",
    response_model=ClientResponse,
    status_code=201
)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    """
    Cria um novo cliente.
    """

    service = ClientService(db)

    return service.create_client(client)