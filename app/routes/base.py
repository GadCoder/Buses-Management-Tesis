from fastapi import APIRouter

from app.routes.v1 import route_bus_company, route_bus, route_bus_route

api_router = APIRouter()
api_router.include_router(
    route_bus_company.router, prefix="/bus-company", tags=["bus_company"]
)
api_router.include_router(route_bus.router, prefix="/bus", tags=["bus"])
api_router.include_router(
    route_bus_route.router, prefix="/bus-route", tags=["bus_route"]
)
