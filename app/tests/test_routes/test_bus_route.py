from tests.utils.bus_route import create_random_bus_route
from tests.utils.bus_company import create_random_bus_company


def test_create_bus_route(client, db_session):
    bus_company = create_random_bus_company(db=db_session)
    data = {"name": "2411", "company_id": bus_company.id}
    response = client.post("/bus-route/create/", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "2411"
    assert response.json()["company_id"] == bus_company.id


def test_should_fetch_bus_route_created(client, db_session):
    bus_route = create_random_bus_route(db=db_session)
    response = client.get(f"/bus-route/get/{bus_route.id}/")
    assert response.status_code == 200
    assert response.json()["name"] == bus_route.name
