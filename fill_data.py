import random
import requests

IS_DEV = True

BASE_URL = "http://127.0.0.1:8000" if IS_DEV else ""


def create_companies():
    companies = ["El Rápido SAC"]
    for company in companies:
        request = requests.post(f"{BASE_URL}/bus-company/create/", json={"name": company})
        if request.status_code != 201:
            print(f"Error creating company {company}")
            return False
    return True


def create_routes():
    routes = ["2411", "8105"]
    for route in routes:
        request = requests.post(f"{BASE_URL}/bus-route/create/", json={"name": route, "company_id": 1})
        if request.status_code != 201:
            print(f"Error creating route {route}")
            return False
    return True


def create_buses():
    plates = ["F5U-456", "G7T-123", "H8Y-789", "I9O-456", "J0P-123", "K1L-789"]
    for plate in plates:
        route_id = random.choice([1, 2])
        request = requests.post(f"{BASE_URL}/bus/create/", json={"plate": plate, "company_id": 1, "route_id": route_id})
        if request.status_code != 201:
            print(f"Error creating bus {plate}")
            return False
    return True


def main():
    created_companies = create_companies()
    if not created_companies:
        print("Error creating companies")
        return
    created_routes = create_routes()
    if not created_routes:
        print("Error creating routes")
        return
    created_buses = create_buses()
    if not created_buses:
        print("Error creating buses")
        return
    print("Data filled successfully")


if __name__ == '__main__':
    main()
