"""
Schemas do Client.

Responsáveis por:
- validar dados de entrada
- padronizar resposta da API
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ClientBase(BaseModel):
    """
    Campos base do cliente.
    """

    name: str = Field(
        min_length=3,
        max_length=120,
        description="Nome completo do cliente"
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15,
        description="Telefone do cliente"
    )


class ClientCreate(ClientBase):
    """
    Schema usado para criação.
    """
    pass


class ClientUpdate(BaseModel):
    """
    Atualização parcial.
    """

    name: Optional[str] = Field(
        min_length=3,
        max_length=120
    )

    phone: Optional[str]


class ClientResponse(ClientBase):
    """
    Retorno da API.
    """

    id: int

    class Config:
        from_attributes = True