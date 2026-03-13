from pydantic import BaseModel, Field


class PaymentCreate(BaseModel):

    client_id: int

    product_id: int

    amount: float = Field(gt=0)