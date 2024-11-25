from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.insurance import InsuranceResponse, InsuranceRequest
from app.crud.rate import rate_by_CargoDatetime
from app.services.kafka_producer import send_log_to_kafka
from datetime import datetime


router = APIRouter()


async def log_insurance_calculation(user_id: int, cargo_type: str, declared_value: float):
    try:
        action = f"Calculated insurance for cargo_type={cargo_type}, declared_value={declared_value}"
        await send_log_to_kafka(
            user_id=user_id,
            action=action,
            timestamp=datetime.utcnow().isoformat()
        )
    except Exception as e:
        print(f"Error logging to Kafka: {e}")


@router.post("/", response_model=InsuranceResponse)
async def calculate_insurance(data: InsuranceRequest, db: Session = Depends(get_db)):
    rate_record = rate_by_CargoDatetime(db, data.cargo_type, datetime.strptime(data.date, "%Y-%m-%d").date())

    if not rate_record:
        raise HTTPException(status_code=404, detail="Rate not found")

    insurance_cost = data.declared_value * rate_record.rate

    await log_insurance_calculation(
        user_id=123,
        cargo_type=data.cargo_type,
        declared_value=data.declared_value
    )

    return InsuranceResponse(insurance_cost=insurance_cost)
