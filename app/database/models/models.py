import uuid
from sqlmodel import SQLModel, Field, Relationship


class BusCompany(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str = Field(unique=True)

    buses: list["Bus"] = Relationship(back_populates="company")
    routes: list["BusRoute"] = Relationship(back_populates="company")


class Bus(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    bus_identifier: uuid.UUID = Field(default_factory=uuid.uuid4)
    plate: str = Field(unique=True)

    company_id: int = Field(foreign_key="buscompany.id")
    route_id: int = Field(foreign_key="busroute.id")
    company: BusCompany = Relationship(back_populates="buses")


class BusRoute(SQLModel, table=True):
    id: int | None = Field(primary_key=True, index=True)
    name: str = Field(max_length=50)

    company_id: int = Field(foreign_key="buscompany.id")
    company: BusCompany = Relationship(back_populates="routes")
