from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String)

    # FK para clinic
    clinic_id = Column(Integer, ForeignKey("clinics.id"))

    # relacionamento com clínica
    clinic = relationship("Clinic", back_populates="clients")

    # relacionamento com pets
    pets = relationship(
    "Pet",
    back_populates="owner",
    cascade="all, delete"
)