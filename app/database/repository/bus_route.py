from sqlalchemy.orm import Session

from schemas.bus_route import BusRouteCreate
from database.models.models import Bus, BusRoute


def create(bus_route: BusRouteCreate, db: Session):
    db_bus_route = BusRoute(**bus_route.model_dump())
    db.add(db_bus_route)
    db.commit()
    db.refresh(db_bus_route)
    return db_bus_route


def get(id: int, db: Session):
    return db.query(BusRoute).filter(BusRoute.id == id).first()


def update(id: int, bus_route: BusRouteCreate, db: Session):
    bus_route_registered = db.query(BusRoute).filter(BusRoute.id == id).first()
    if not bus_route_registered:
        return None
    bus_route_registered.name = bus_route.name
    db.add(bus_route_registered)
    db.commit()
    db.refresh(bus_route_registered)
    return bus_route_registered


def delete(id: int, db: Session):
    bus_route_registered = db.query(BusRoute).filter(BusRoute.id == id)
    if not bus_route_registered.first():
        return {"error": f"Bus Route  with id {id} not found"}
    bus_route_registered.delete()
    db.commit()
    return {"message": f"Bus Route with id {id} deleted successfully"}


def get_all(db: Session):
    return db.query(BusRoute).all()


def delete_all_from_company(company_id: int, db: Session):
    db.query(BusRoute).filter(BusRoute.company_id == company_id).delete()
    db.commit()
    return {"message": f"All Bus Routes from company with id {id} deleted successfully"}


def get_buses_from_route(route_id: int, db: Session):
    return db.query(Bus).filter(Bus.route_id == route_id).all()
