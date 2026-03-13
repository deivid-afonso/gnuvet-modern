"""
Representa animais cadastrados no sistema
"""

from pydantic import BaseModel, Field, ConfigDict


class PetCreate(BaseModel):

    name: str = Field(min_length=2)

    species: str = Field(
        description="Ex: dog, cat"
    )

    breed: str

    age: int = Field(
        ge=0,
        le=40
    )

    owner_id: int


class PetResponse(BaseModel):

    id: int

    name: str

    species: str

    breed: str

    age: int

    owner_id: int

    model_config = ConfigDict(from_attributes=True)