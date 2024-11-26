from sqlalchemy.orm import Session

from schemas.bus_company import BusCompanyCreate
from database.models.models import BusCompany
from .bus import delete_all_from_company as delete_buses_from_company
from .bus_route import delete_all_from_company as delete_routes_from_company


def create(bus_company: BusCompanyCreate, db: Session):
    db_bus_company = BusCompany(**bus_company.model_dump())
    db.add(db_bus_company)
    db.commit()
    db.refresh(db_bus_company)
    return db_bus_company


def get(id: int, db: Session):
    return db.query(BusCompany).filter(BusCompany.id == id).first()


def update(id: int, bus_company: BusCompanyCreate, db: Session):
    bus_company_registered = db.query(BusCompany).filter(BusCompany.id == id).first()
    if not bus_company_registered:
        return None
    bus_company_registered.name = bus_company.name
    db.add(bus_company_registered)
    db.commit()
    db.refresh(bus_company_registered)
    return bus_company_registered


def delete(id: int, db: Session):
    bus_company_registered = db.query(BusCompany).filter(BusCompany.id == id)
    if not bus_company_registered.first():
        return {"error": f"Bus Company  with id {id} not found"}
    bus_company_registered.delete()
    db.commit()
    delete_buses_from_company(id, db)
    delete_routes_from_company(id, db)
    return {"message": f"Bus Company with id {id} deleted successfully"}


def get_all(db: Session):
    return db.query(BusCompany).all()


def get_from_name(name: str, db: Session):
    return db.query(BusCompany).filter(BusCompany.name == name).all()
