from sqlalchemy.orm import Session

from schemas.bus_route import BusRouteCreate
from database.repository.bus_route import create


def create_random_bus_route(db: Session):
    bus_route = BusRouteCreate(name="2411", company_id=1)
    created_bus_route = create(bus_route=bus_route, db=db)
    return created_bus_route
