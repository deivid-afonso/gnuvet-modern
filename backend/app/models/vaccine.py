"""
Controle de vacinação dos pets
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base


class Vaccine(Base):

    __tablename__ = "vaccines"

    id = Column(Integer, primary_key=True)

    pet_id = Column(Integer, ForeignKey("pets.id"))

    name = Column(String)

    date_applied = Column(DateTime)

    next_due = Column(DateTime)

    pet = relationship("Pet")