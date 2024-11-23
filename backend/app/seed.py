import json
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.rate import Cargo, Rate
from app.core.database import get_db


def load_data_from_json(json_file: str, db: Session):
    with open(json_file, "r") as file:
        data = json.load(file)

    for date_str, rates in data.items():
        effective_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        for rate_entry in rates:
            cargo_type = rate_entry["cargo_type"]
            rate_value = rate_entry["rate"]

            cargo = db.query(Cargo).filter(Cargo.name == cargo_type).first()
            if not cargo:
                cargo = Cargo(name=cargo_type)
                db.add(cargo)
                db.commit()
                db.refresh(cargo)

            rate = Rate(cargo_id=cargo.id, rate=rate_value, effective_date=effective_date)
            db.add(rate)

        db.commit()

    print("Data loaded successfully!")


def main():
    db = next(get_db())

    load_data_from_json("app/rates_data.json", db)


if __name__ == "__main__":
    main()
