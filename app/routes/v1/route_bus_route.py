from fastapi import APIRouter, HTTPException, status

from schemas.bus import BusShow
from schemas.bus_route import BusRouteCreate, BusRouteShow
from database.session import SessionDep
from database.repository import bus_route as bus_route_repo

router = APIRouter()


@router.post(
    "/create/", response_model=BusRouteShow, status_code=status.HTTP_201_CREATED
)
async def create_bus_route(bus_route: BusRouteCreate, session: SessionDep):
    print(bus_route.company_id)
    return bus_route_repo.create(bus_route=bus_route, session=session)


@router.get("/get/{id}/", response_model=BusRouteShow)
async def get_bus_route(id: int, session: SessionDep):
    bus_route = bus_route_repo.get(id=id, session=session)
    if not bus_route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus Route with id {id} not found",
        )
    return bus_route


@router.put("/update/{id}/", response_model=BusRouteShow)
def update_bus_route(id: int, bus_route: BusRouteCreate, session: SessionDep):
    bus_route = bus_route_repo.update(id=id, bus_route=bus_route, session=session)
    if not bus_route:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus Route with id {id} not found",
        )
    return bus_route


@router.delete("/delete/{id}/")
def delete_bus_route(id: int, session: SessionDep):
    message = bus_route_repo.delete(id=id, session=session)
    if message.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.get("error"),
        )

    return {"msg": f"Bus Route with id {id} deleted successfully"}


@router.get("/get-all/", response_model=list[BusRouteShow])
def get_all_buses_routes(session: SessionDep):
    return bus_route_repo.get_all(session=session)


@router.get("/get-buses-from-route/", response_model=list[BusShow])
def get_buses_from_route(route_id: int, session: SessionDep):
    return bus_route_repo.get_buses_from_route(route_id=route_id, session=session)
