from http.client import HTTPException
from typing import Type
from sqlalchemy.orm import Session, joinedload
from app.models.rate import Rate, Cargo
from app.schemas.rate import RateCreate, RateUpdate
from datetime import date


def rate_by_CargoDatetime(db: Session, cargo_type: str, current_date: date) -> Rate | None:
    """
    Получить актуальный тариф для указанного типа груза и даты.
    :param db: Сессия базы данных
    :param cargo_type: Тип груза
    :param current_date: Текущая дата, для которой ищется тариф
    :return: Тариф или None, если ничего не найдено
    """
    return (
        db.query(Rate)
        .join(Rate.cargo)
        .filter(Cargo.name == cargo_type)
        .filter(Rate.effective_date <= current_date)
        .order_by(Rate.effective_date.desc())
        .first()
    )


def get_rates(db: Session, skip: int = 0, limit: int = 10) -> list[Type[Rate]]:
    """
    Получить список тарифов с поддержкой пагинации.
    :param db: Сессия базы данных
    :param skip: Количество записей для пропуска (начало пагинации)
    :param limit: Максимальное количество записей для возврата
    :return: Список объектов Rate
    """
    return db.query(Rate).options(joinedload(Rate.cargo)).offset(skip).limit(limit).all()


def get_rate_by_id(db: Session, rate_id: int) -> Rate | None:
    """
    Получить тариф по его ID.
    :param db: Сессия базы данных
    :param rate_id: Идентификатор тарифа
    :return: Объект Rate или None, если не найден
    """
    return db.query(Rate).filter(Rate.id == rate_id).first()


def create_rate(db: Session, rate_data: RateCreate):
    """
    Создать новую запись о тарифе, связывая с cargo_id.

    :param db: Сессия базы данных
    :param rate_data: Данные для создания тарифа
    :return: Созданный объект Rate
    """
    db_rate = Rate(
        cargo_id=rate_data.cargo_id,
        rate=rate_data.rate,
        effective_date=rate_data.effective_date,
    )
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate


def update_rate(db: Session, rate_id: int, rate_data: RateUpdate):
    """
    Обновить запись о тарифе.

    :param db: Сессия базы данных
    :param rate_id: ID обновляемого тарифа
    :param rate_data: Данные для обновления
    :return: Обновленный объект Rate
    """

    db_rate = db.query(Rate).filter(Rate.id == rate_id).first()

    if not db_rate:
        raise HTTPException(status_code=404, detail="Rate not found")

    for key, value in rate_data.dict(exclude_unset=True).items():
        if key == "cargo_id":
            db_rate.cargo_id = value
        else:
            setattr(db_rate, key, value)

    db.commit()
    db.refresh(db_rate)
    return db_rate


def delete_rate(db: Session, rate_id: int):
    db_rate = db.query(Rate).filter(Rate.id == rate_id).first()
    db.delete(db_rate)
    db.commit()
    return db_rate
