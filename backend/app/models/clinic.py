from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.base import Base

class Clinic(Base):

    __tablename__ = "clinics"

    id = Column(Integer, primary_key=True)

    name = Column(String(120), nullable=False)

    address = Column(String(200))

    phone = Column(String(15))

    users = relationship("User", back_populates="clinic")

    clients = relationship("Client", back_populates="clinic")