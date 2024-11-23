from pydantic import BaseModel


class InsuranceRequest(BaseModel):
    cargo_type: str
    declared_value: float
    date: str


class InsuranceResponse(BaseModel):
    insurance_cost: float

    class Config:
        from_attributes = True
