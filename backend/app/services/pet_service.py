"""
Pet Service

Camada de serviço responsável pela lógica de negócio
relacionada aos pets.

A camada de service fica entre:
routes → services → repository/model
"""

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.pet import Pet
from app.models.client import Client


def create_pet(db: Session, pet_data):
    """
    Cria um novo pet.

    Valida se o dono (client) existe antes de criar o pet.
    """

    owner = db.query(Client).filter(Client.id == pet_data.owner_id).first()

    if not owner:
        raise HTTPException(
            status_code=404,
            detail="Owner not found"
        )

    pet = Pet(**pet_data.model_dump())

    db.add(pet)
    db.commit()
    db.refresh(pet)

    return pet