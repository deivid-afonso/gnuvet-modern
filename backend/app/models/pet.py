from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Pet(Base):

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    species = Column(String, nullable=False)

    breed = Column(String)

    age = Column(Integer)

    owner_id = Column(Integer, ForeignKey("clients.id"))

    owner = relationship("Client", back_populates="pets")