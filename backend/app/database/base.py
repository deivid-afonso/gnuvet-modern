"""
Base declarativa do SQLAlchemy.
Todos os models devem herdar dela.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass