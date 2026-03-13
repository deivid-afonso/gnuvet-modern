from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database.base import Base

class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)

    amount = Column(Float)

    client_id = Column(Integer, ForeignKey("clients.id"))

    product_id = Column(Integer, ForeignKey("products.id"))