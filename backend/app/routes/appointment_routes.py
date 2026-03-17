"""
Rotas de consultas veterinárias
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.appointment_service import AppointmentService
from app.schemas.appointment_schema import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/")
def create_appointment(data: AppointmentCreate, db: Session = Depends(get_db)):
    service = AppointmentService(db)
    return service.create(data)