from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.rate import RateCreate, RateUpdate, Rate
from app.core.database import get_db
from app.crud.rate import (
    get_rates,
    get_rate_by_id,
    create_rate,
    update_rate,
    delete_rate,
)


router = APIRouter()


@router.get("/", response_model=list[Rate])
def read_rates(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получить список всех тарифов с поддержкой пагинации.
    """
    rates = get_rates(db, skip=skip, limit=limit)
    return rates


@router.get("/{rate_id}", response_model=Rate)
def read_rate(rate_id: int, db: Session = Depends(get_db)):
    """
    Получить тариф по его ID.
    """
    rate = get_rate_by_id(db, rate_id=rate_id)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return rate


@router.post("/", response_model=Rate)
def create_new_rate(rate_data: RateCreate, db: Session = Depends(get_db)):
    """
    Создать новый тариф.
    """
    return create_rate(db, rate_data=rate_data)


@router.put("/{rate_id}", response_model=Rate)
def update_existing_rate(rate_id: int, rate_data: RateUpdate, db: Session = Depends(get_db)):
    """
    Обновить существующий тариф по ID.
    """
    rate = get_rate_by_id(db, rate_id=rate_id)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    return update_rate(db, rate_id=rate_id, rate_data=rate_data)


@router.delete("/{rate_id}")
def delete_rate_endpoint(rate_id: int, db: Session = Depends(get_db)):
    """
    Удалить тариф по ID.
    """
    rate = get_rate_by_id(db, rate_id=rate_id)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")
    delete_rate(db, rate_id=rate_id)
    return {"detail": f"Rate with id {rate_id} has been deleted"}
