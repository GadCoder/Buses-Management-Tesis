from sqlmodel import SQLModel
from app.schemas.bus_route import BusRouteShow


class BusCompanyBase(SQLModel):
    name: str


class BusCompanyCreate(BusCompanyBase):
    pass


class BusCompanyShow(BusCompanyBase):
    id: int
    routes: list[BusRouteShow]


class BusCompanyUpdate(BusCompanyCreate):
    pass
