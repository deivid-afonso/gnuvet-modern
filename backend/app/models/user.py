from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)

    password_hash = Column(String)

    role = Column(String)

    clinic_id = Column(Integer, ForeignKey("clinics.id"))

    clinic = relationship("Clinic", back_populates="users")