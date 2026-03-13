"""
Service responsável pelas regras de negócio
da entidade Client.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.client import Client
from app.repository.client_repository import ClientRepository
from app.schemas.client_schema import ClientCreate


class ClientService:

    def __init__(self, db: Session):

        self.repo = ClientRepository(db)

    def list_clients(self):

        return self.repo.get_all()

    def create_client(self, data: ClientCreate):

        existing = self.repo.get_by_email(data.email)

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Client with this email already exists"
            )

        client = Client(**data.model_dump())

        return self.repo.create(client)