from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.base import Base

class Vaccine(Base):

    __tablename__ = "vaccines"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    application_date = Column(Date)

    next_due_date = Column(Date)

    pet_id = Column(Integer, ForeignKey("pets.id"))