from pydantic import BaseModel


class MedicalRecordCreate(BaseModel):

    pet_id: int

    diagnosis: str

    treatment: str

    notes: str | None