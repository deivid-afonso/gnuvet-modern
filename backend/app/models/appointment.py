from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base

class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    pet_id = Column(Integer, ForeignKey("pets.id"))

    date = Column(DateTime)

    pet = relationship("Pet")