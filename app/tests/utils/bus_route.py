from sqlmodel import Session
from app.schemas.bus_route import BusRouteCreate
from app.database.repository.bus_route import create


def create_random_bus_route(session: Session):
    bus_route = BusRouteCreate(name="2411", company_id=1)
    created_bus_route = create(bus_route=bus_route, db=session)
    return created_bus_route
