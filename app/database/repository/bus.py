from sqlmodel import select
from app.schemas.bus import BusCreate
from app.database.models.models import Bus

from app.database.session import SessionDep


def create(bus: BusCreate, session: SessionDep):
    session_bus = Bus(**bus.model_dump())
    session.add(session_bus)
    session.commit()
    session.refresh(session_bus)
    return session_bus


def get(id: int, session: SessionDep):
    return session.get(Bus, id)


def update(id: int, bus: BusCreate, session: SessionDep):
    bus_registered = session.get(Bus, id)
    if not bus_registered:
        return None
    bus_registered.name = bus.name
    session.add(bus_registered)
    session.commit()
    session.refresh(bus_registered)
    return bus_registered


def delete(id: int, session: SessionDep):
    bus_registered = session.get(Bus, id)
    if not bus_registered.first():
        return {"error": f"Bus with id {id} not found"}
    bus_registered.delete()
    session.commit()
    return {"message": f"Buswith id {id} deleted successfully"}


def get_all(session: SessionDep):
    return session.exec(select(Bus)).all()


def delete_all_from_company(company_id: int, session: SessionDep):
    session.query(select(Bus)).filter(Bus.company_id == company_id).delete()
    session.commit()
    return {"message": f"All Buses from company with id {id} deleted successfully"}


def get_from_company(bus_company_id: int, session: SessionDep):
    return session.exec(select(Bus)).filter(Bus.company_id == bus_company_id).all()


def get_from_route(company_id: int, session: SessionDep):
    return session.exec(select(Bus)).filter(Bus.company_id == company_id).all()
