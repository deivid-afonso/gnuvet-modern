"""
Importa todos os models para o SQLAlchemy
reconhecer as tabelas.
"""

from app.models.client import Client
from app.models.pet import Pet
from app.models.clinic import Clinic
from app.models.user import User
from app.models.appointment import Appointment
from app.models.medical_record import MedicalRecord
from app.models.vaccine import Vaccine
from app.models.product import Product
from app.models.payment import Payment