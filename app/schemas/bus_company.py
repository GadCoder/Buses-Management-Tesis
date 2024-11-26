from sqlmodel import SQLModel
from schemas.bus_route import BusRouteShow


class BusCompanyBase(SQLModel):
    name: str


class BusCompanyCreate(BusCompanyBase):
    pass


class BusCompanyShow(BusCompanyBase):
    id: int
    routes: list[BusRouteShow]


class BusCompanyUpdate(BusCompanyCreate):
    pass
