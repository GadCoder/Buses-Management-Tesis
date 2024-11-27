from sqlalchemy.orm import Session

from app.schemas.bus_route import BusRouteCreate
from app.database.models.models import Bus, BusRoute


def create(bus_route: BusRouteCreate, session: Session):
    session_bus_route = BusRoute(**bus_route.model_dump())
    session.add(session_bus_route)
    session.commit()
    session.refresh(session_bus_route)
    return session_bus_route


def get(id: int, session: Session):
    return session.get(BusRoute, id)


def update(id: int, bus_route: BusRouteCreate, session: Session):
    bus_route_registered = session.get(BusRoute, id)
    if not bus_route_registered:
        return None
    bus_route_registered.name = bus_route.name
    session.add(bus_route_registered)
    session.commit()
    session.refresh(bus_route_registered)
    return bus_route_registered


def delete(id: int, session: Session):
    bus_route_registered = session.get(BusRoute, id)
    if not bus_route_registered.first():
        return {"error": f"Bus Route  with id {id} not found"}
    bus_route_registered.delete()
    session.commit()
    return {"message": f"Bus Route with id {id} deleted successfully"}


def get_all(session: Session):
    return session.query(BusRoute).all()


def delete_all_from_company(company_id: int, session: Session):
    session.query(BusRoute).filter(BusRoute.company_id == company_id).delete()
    session.commit()
    return {"message": f"All Bus Routes from company with id {id} deleted successfully"}


def get_buses_from_route(route_id: int, session: Session):
    return session.query(Bus).filter(Bus.route_id == route_id).all()
