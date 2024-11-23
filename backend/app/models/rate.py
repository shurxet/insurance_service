from sqlalchemy import Column, String, Float, Date, Integer, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship


class Cargo(Base):
    __tablename__ = 'cargo'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    rates = relationship("Rate", back_populates="cargo", cascade="all, delete-orphan")


class Rate(Base):
    __tablename__ = 'rates'

    id = Column(Integer, primary_key=True, index=True)
    rate = Column(Float, nullable=False)
    effective_date = Column(Date, nullable=False)
    cargo_id = Column(Integer, ForeignKey('cargo.id'), nullable=False)

    cargo = relationship("Cargo", back_populates="rates")
