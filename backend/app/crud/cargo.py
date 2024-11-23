from http.client import HTTPException
from typing import Type
from sqlalchemy.orm import Session
from app.models.rate import Cargo
from app.schemas.cargo import CargoCreate, CargoUpdate


def get_cargos(db: Session) -> list[Type[Cargo]]:
    """
    Получить список грузов.
    :param db: Сессия базы данных
    :return: Список объектов Cargo
    """
    return db.query(Cargo).all()


def get_cargo_by_id(db: Session, cargo_id: int):
    db_cargo = db.query(Cargo).filter(Cargo.id == cargo_id).first()

    return db_cargo


def create_cargo(db: Session, cargo_data: CargoCreate):
    """
    Создать новый груз для последующий его привязки к тарифу.

    :param db: Сессия базы данных
    :param cargo_data: Данные для создания груза
    :return: Созданный объект Cargo
    """
    db_cargo = Cargo(
        name=cargo_data.name
    )
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo


def update_cargo(db: Session, cargo_id: int, cargo_data: CargoUpdate):
    """
    Обновить запись о грузе.

    :param db: Сессия базы данных
    :param cargo_id: ID обновляемого груза
    :param cargo_data: Данные для обновления
    :return: Обновленный объект Cargo
    """
    db_cargo = db.query(Cargo).filter(Cargo.id == cargo_id).first()

    if not db_cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")

    for key, value in cargo_data.dict(exclude_unset=True).items():
        setattr(db_cargo, key, value)

    db.commit()
    db.refresh(db_cargo)
    return db_cargo


def delete_cargo(db: Session, cargo_id: int):
    db_cargo = db.query(Cargo).filter(Cargo.id == cargo_id).first()
    db.delete(db_cargo)
    db.commit()
    return db_cargo
