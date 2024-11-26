from sqlmodel import Field, SQLModel


class BusRouteBase(SQLModel):
    name: str = Field(..., max_length=50)
    company_id: int


class BusRouteCreate(BusRouteBase):
    pass


class BusRouteShow(BusRouteBase):
    id: int
