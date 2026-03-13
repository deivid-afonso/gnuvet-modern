from pydantic import BaseModel
from datetime import date


class VaccineCreate(BaseModel):

    name: str

    application_date: date

    next_due_date: date

    pet_id: int