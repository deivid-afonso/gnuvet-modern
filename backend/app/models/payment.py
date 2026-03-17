"""
Pagamentos realizados na clínica
"""

from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)

    appointment_id = Column(Integer, ForeignKey("appointments.id"))

    amount = Column(Float)

    method = Column(String)

    appointment = relationship("Appointment")