"""
Schemas pydantic das consultas
"""

from pydantic import BaseModel
from datetime import datetime


class AppointmentCreate(BaseModel):

    pet_id: int
    user_id: int
    date: datetime