from sqlmodel import Session

from app.schemas.bus import BusCreate
from app.database.repository.bus import create
from app.tests.utils.bus_company import create_random_bus_company
from app.tests.utils.bus_route import create_random_bus_route


def create_random_bus(session: Session):
    bus_company = create_random_bus_company(session=session)
    bus_route = create_random_bus_route(session=session)
    bus = BusCreate(plate="ABC-123", company_id=bus_company.id, route_id=bus_route.id)
    created_bus = create(bus=bus, session=session)
    return created_bus
