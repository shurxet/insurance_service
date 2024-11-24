from pydantic import BaseModel
from datetime import datetime


class InsuranceRequest(BaseModel):
    cargo_type: str
    declared_value: float
    date: str


class InsuranceResponse(BaseModel):
    insurance_cost: float

    class Config:
        from_attributes = True


class InsuranceLogCreate(BaseModel):
    cargo_id: int
    action: str
    insurance_cost: float
    timestamp: datetime
