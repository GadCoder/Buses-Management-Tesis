from fastapi import APIRouter, HTTPException, status

from app.database.session import SessionDep
from app.schemas.bus import BusCreate, BusShow
from app.database.repository import bus as bus_repo

router = APIRouter()


@router.post("/create/", response_model=BusShow, status_code=status.HTTP_201_CREATED)
async def create_bus(bus: BusCreate, session: SessionDep):
    return bus_repo.create(bus=bus, session=session)


@router.get("/get/{id}/", response_model=BusShow)
async def get_bus(id: int, session: SessionDep):
    bus = bus_repo.get(id=id, session=session)
    if not bus:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus with id {id} not found",
        )
    return bus


@router.put("/update/{id}/", response_model=BusShow)
def update_bus(id: int, bus: BusCreate, session: SessionDep):
    bus = bus_repo.update(id=id, bus=bus, session=session)
    if not bus:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus with id {id} not found",
        )
    return bus


@router.delete("/delete/{id}/", response_model=BusShow)
def delete_bus(id: int, session: SessionDep):
    message = bus_repo.delete(id=id, session=session)
    if message.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.get("error"),
        )

    return {"msg": f"Bus with id {id} deleted successfully"}


@router.get("/get-all/", response_model=list[BusShow])
def get_all_buses(session: SessionDep):
    return bus_repo.get_all(session=session)
