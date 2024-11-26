from sqlalchemy.orm import Session

from database.repository.bus import create
from schemas.bus import BusCreate
from tests.utils.bus_company import create_random_bus_company
from tests.utils.bus_route import create_random_bus_route


def create_random_bus(db: Session):
    bus_company = create_random_bus_company(db=db)
    bus_route = create_random_bus_route(db=db)
    bus = BusCreate(plate="ABC-123", company_id=bus_company.id, route_id=bus_route.id)
    created_bus = create(bus=bus, db=db)
    return created_bus
