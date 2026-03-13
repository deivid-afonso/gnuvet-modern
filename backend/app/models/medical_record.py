from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class MedicalRecord(Base):

    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True)

    pet_id = Column(Integer, ForeignKey("pets.id"))

    diagnosis = Column(String)

    treatment = Column(String)

    notes = Column(String)