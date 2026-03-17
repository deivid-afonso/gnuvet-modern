"""
Modelo responsável por representar
consultas veterinárias agendadas.
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.database.base import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    # pet da consulta
    pet_id = Column(Integer, ForeignKey("pets.id"))

    # veterinário responsável
    user_id = Column(Integer, ForeignKey("users.id"))

    # data da consulta
    date = Column(DateTime, nullable=False)

    # status
    status = Column(String, default="scheduled")

    # relacionamentos
    pet = relationship("Pet")
    user = relationship("User")