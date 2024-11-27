from sqlalchemy.orm import Session

from app.schemas.bus_company import BusCompanyCreate
from app.database.models.models import BusCompany
from .bus import delete_all_from_company as delete_buses_from_company
from .bus_route import delete_all_from_company as delete_routes_from_company


def create(bus_company: BusCompanyCreate, session: Session):
    session_bus_company = BusCompany(**bus_company.model_dump())
    session.add(session_bus_company)
    session.commit()
    session.refresh(session_bus_company)
    return session_bus_company


def get(id: int, session: Session):
    return session.get(BusCompany, id)


def update(id: int, bus_company: BusCompanyCreate, session: Session):
    bus_company_registered = session.get(BusCompany, id)
    if not bus_company_registered:
        return None
    bus_company_registered.name = bus_company.name
    session.add(bus_company_registered)
    session.commit()
    session.refresh(bus_company_registered)
    return bus_company_registered


def delete(id: int, session: Session):
    bus_company_registered = session.query(BusCompany).filter(BusCompany.id == id)
    if not bus_company_registered.first():
        return {"error": f"Bus Company  with id {id} not found"}
    bus_company_registered.delete()
    session.commit()
    delete_buses_from_company(id, session)
    delete_routes_from_company(id, session)
    return {"message": f"Bus Company with id {id} deleted successfully"}


def get_all(session: Session):
    return session.query(BusCompany).all()


def get_from_name(name: str, session: Session):
    return session.query(BusCompany).filter(BusCompany.name == name).all()
