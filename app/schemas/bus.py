from uuid import UUID
from sqlmodel import Field, SQLModel


class BusBase(SQLModel):
    plate: str = Field(..., max_length=7)
    company_id: int
    route_id: int


class BusCreate(BusBase):
    pass


class BusShow(BusBase):
    bus_identifier: UUID
