"""
Regras de negócio das consultas
"""

from app.repository.appointment_repository import AppointmentRepository
from app.models.appointment import Appointment


class AppointmentService:

    def __init__(self, db):
        self.repo = AppointmentRepository(db)

    def create(self, data):
        appointment = Appointment(**data.model_dump())
        return self.repo.create(appointment)