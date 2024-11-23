from pydantic import BaseModel


class CargoBase(BaseModel):
    name: str


class CargoCreate(CargoBase):
    pass


class CargoUpdate(CargoBase):
    pass


class Cargo(CargoBase):
    id: int
    name: str

    class Config:
        from_attributes = True
