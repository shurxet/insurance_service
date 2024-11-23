from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.cargo import get_cargos, create_cargo, delete_cargo, get_cargo_by_id, update_cargo
from app.schemas.cargo import Cargo, CargoCreate, CargoUpdate
from app.core.database import get_db

router = APIRouter()


@router.get("/", response_model=list[Cargo])
def read_cargos(db: Session = Depends(get_db)):
    """
    Получить список всех грузов.
    """
    cargos = get_cargos(db)
    return cargos


@router.get("/{cargo_id}", response_model=Cargo)
def read_cargo(cargo_id: int, db: Session = Depends(get_db)):
    """
    Получить груз по его ID.
    """
    cargo = get_cargo_by_id(db, cargo_id=cargo_id)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return cargo


@router.post("/", response_model=Cargo)
def create_new_сargo(cargo_data: CargoCreate, db: Session = Depends(get_db)):
    """
    Создать новый груз.
    """
    return create_cargo(db, cargo_data=cargo_data)


@router.put("/{cargo_id}", response_model=Cargo)
def update_existing_cargo(cargo_id: int, cargo_data: CargoUpdate, db: Session = Depends(get_db)):
    """
    Обновить существующий груз по ID.
    """
    cargo = get_cargo_by_id(db, cargo_id=cargo_id)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    return update_cargo(db, cargo_id=cargo_id, cargo_data=cargo_data)


@router.delete("/{cargo_id}")
def delete_cargo_endpoint(cargo_id: int, db: Session = Depends(get_db)):
    """
    Удалить груз по ID.
    """
    cargo = get_cargo_by_id(db, cargo_id=cargo_id)
    if not cargo:
        raise HTTPException(status_code=404, detail="Cargo not found")
    delete_cargo(db, cargo_id=cargo_id)
    return {"detail": f"Cargo with id {cargo_id} has been deleted"}
