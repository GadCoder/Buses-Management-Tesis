from sqlalchemy.orm import Session

from schemas.bus_company import BusCompanyCreate
from database.repository.bus_company import create


def create_random_bus_company(db: Session):
    bus_company = BusCompanyCreate(name="El Rapido SAC")
    created_bus_company = create(bus_company=bus_company, db=db)
    return created_bus_company
