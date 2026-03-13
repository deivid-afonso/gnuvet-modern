"""
Pet Routes

Define endpoints relacionados a pets.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.pet_schema import PetCreate
from app.services import pet_service

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)


@router.post("/", status_code=201)
def create_pet(
    pet: PetCreate,
    db: Session = Depends(get_db)
):
    """
    Endpoint para criar um novo pet.
    """

    return pet_service.create_pet(db, pet)