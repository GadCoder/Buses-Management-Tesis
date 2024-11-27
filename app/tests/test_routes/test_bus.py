from app.tests.utils.bus import create_random_bus
from app.tests.utils.bus_route import create_random_bus_route
from app.tests.utils.bus_company import create_random_bus_company


def test_create_bus(client, session):
    bus_company = create_random_bus_company(session=session)
    bus_route = create_random_bus_route(session=session)
    data = {
        "plate": "ABC-123",
        "company_id": bus_company.id,
        "route_id": bus_route.id,
    }
    response = client.post("/bus/create/", json=data)
    assert response.status_code == 201
    assert response.json()["plate"] == "ABC-123"
    assert response.json()["company_id"] == bus_company.id
    assert response.json()["route_id"] == bus_route.id


def test_should_fetch_bus_created(client, session):
    bus = create_random_bus(session=session)
    response = client.get(f"/bus/get/{bus.id}/")
    assert response.status_code == 200
    assert response.json()["plate"] == bus.plate
