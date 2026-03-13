from pydantic import BaseModel
from datetime import datetime


class AppointmentCreate(BaseModel):

    pet_id: int

    veterinarian_id: int

    date: datetime

    notes: str | None = None


class AppointmentResponse(BaseModel):

    id: int

    pet_id: int

    veterinarian_id: int

    date: datetime