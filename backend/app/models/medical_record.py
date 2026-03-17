"""
Prontuário veterinário do pet
"""

from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base


class MedicalRecord(Base):

    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True)

    pet_id = Column(Integer, ForeignKey("pets.id"))

    description = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)

    pet = relationship("Pet")