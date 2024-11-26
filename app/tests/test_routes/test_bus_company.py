def test_create_bus_company(client):
    data = {"name": "El Rapido SAC"}
    response = client.post("/bus-company/create/", json=data)
    assert response.status_code == 201
    assert response.json()["name"] == "El Rapido SAC"
