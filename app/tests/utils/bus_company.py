from sqlmodel import Session
from app.schemas.bus_company import BusCompanyCreate
from app.database.repository.bus_company import create


def create_random_bus_company(session: Session):
    bus_company = BusCompanyCreate(name="El Rapido SAC")
    created_bus_company = create(bus_company=bus_company, session=session)
    return created_bus_company
