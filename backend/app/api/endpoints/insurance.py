from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.insurance import InsuranceResponse, InsuranceRequest
from app.crud.rate import rate_by_CargoDatetime


router = APIRouter()


@router.post("/", response_model=InsuranceResponse)
def calculate_insurance(data: InsuranceRequest, db: Session = Depends(get_db)):
    rate_record = rate_by_CargoDatetime(db, data.cargo_type, datetime.strptime(data.date, "%Y-%m-%d").date())
    if not rate_record:
        raise HTTPException(status_code=404, detail="Rate not found")
    insurance_cost = data.declared_value * rate_record.rate
    return InsuranceResponse(insurance_cost=insurance_cost)
