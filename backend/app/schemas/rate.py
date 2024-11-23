from pydantic import BaseModel
from datetime import date

from app.schemas.cargo import CargoBase


class RateBase(BaseModel):
    rate: float
    effective_date: date


class RateCreate(RateBase):
    cargo_id: int


class RateUpdate(BaseModel):
    cargo_id: int
    rate: float | None = None
    effective_date: date | None = None


class Rate(RateBase):
    id: int
    cargo: CargoBase

    class Config:
        from_attributes = True
