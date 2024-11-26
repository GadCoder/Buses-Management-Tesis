from tests.utils.bus import create_random_bus
from tests.utils.bus_route import create_random_bus_route
from tests.utils.bus_company import create_random_bus_company


def test_create_bus(client, db_session):
    bus_company = create_random_bus_company(db=db_session)
    bus_route = create_random_bus_route(db=db_session)
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


def test_should_fetch_bus_created(client, db_session):
    bus = create_random_bus(db=db_session)
    response = client.get(f"/bus/get/{bus.id}/")
    assert response.status_code == 200
    assert response.json()["plate"] == bus.plate
