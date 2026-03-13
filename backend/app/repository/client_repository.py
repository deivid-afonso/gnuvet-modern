"""
Repository responsável pelo acesso ao banco
para entidade Client.
"""

from sqlalchemy.orm import Session
from app.models.client import Client


class ClientRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        """
        Retorna todos os clientes.
        """
        return self.db.query(Client).all()

    def get_by_id(self, client_id: int):
        """
        Busca cliente por ID.
        """
        return (
            self.db
            .query(Client)
            .filter(Client.id == client_id)
            .first()
        )

    def get_by_email(self, email: str):
        """
        Busca cliente por email.
        """
        return (
            self.db
            .query(Client)
            .filter(Client.email == email)
            .first()
        )

    def create(self, client: Client):

        self.db.add(client)

        self.db.commit()

        self.db.refresh(client)

        return client

    def delete(self, client: Client):

        self.db.delete(client)

        self.db.commit()