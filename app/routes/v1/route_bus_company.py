from fastapi import APIRouter, HTTPException, status

from app.database.session import SessionDep
from app.schemas.bus_company import BusCompanyCreate, BusCompanyShow
from app.database.repository import bus_company as bus_company_repo

router = APIRouter()


@router.post(
    "/create/", response_model=BusCompanyShow, status_code=status.HTTP_201_CREATED
)
async def create_bus_company(bus_company: BusCompanyCreate, session: SessionDep):
    return bus_company_repo.create(bus_company=bus_company, session=session)


@router.get("/get/{id}/", response_model=BusCompanyShow)
async def get_bus_company(id: int, session: SessionDep):
    bus_company = bus_company_repo.get(id=id, session=session)
    if not bus_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus Company with id {id} not found",
        )
    return bus_company


@router.put("/update/{id}/", response_model=BusCompanyShow)
def update_bus_company(id: int, bus_company: BusCompanyCreate, session: SessionDep):
    bus_company = bus_company_repo.update(
        id=id, bus_company=bus_company, session=session
    )
    if not bus_company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bus Company with id {id} not found",
        )
    return bus_company


@router.delete("/delete/{id}/")
def delete_bus_company(id: int, session: SessionDep):
    message = bus_company_repo.delete(id=id, session=session)
    if message.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.get("error"),
        )

    return {"msg": f"Bus Company with id {id} deleted successfully"}


@router.get("/get-all/", response_model=list[BusCompanyShow])
def get_all_bus_companies(session: SessionDep):
    return bus_company_repo.get_all(session=session)
