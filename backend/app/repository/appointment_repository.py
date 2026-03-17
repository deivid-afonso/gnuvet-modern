"""
Camada de acesso ao banco
para consultas veterinárias
"""


class AppointmentRepository:

    def __init__(self, db):
        self.db = db

    def create(self, appointment):

        self.db.add(appointment)
        self.db.commit()
        self.db.refresh(appointment)

        return appointment