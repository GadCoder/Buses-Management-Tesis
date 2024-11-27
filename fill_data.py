import string
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


def create_buses(route_id: int):
    for x in range(50):
        plate = generate_random_plate()
        request = requests.post(f"{BASE_URL}/bus/create/", json={"plate": plate, "company_id": 1, "route_id": route_id})
        if request.status_code != 201:
            print(f"Error creating bus {plate} for route {route_id}")
            return False
    return True


def generate_random_plate():
    # Generate a random uppercase letter
    letter = random.choice(string.ascii_uppercase)
    # Generate a random digit
    digit = random.randint(0, 9)
    # Generate a random 3-digit number
    number = ''.join(random.choices(string.digits, k=3))
    # Combine the parts to create the string
    return f"{letter}{digit}{letter}-{number}"


def main():
    created_companies = create_companies()
    if not created_companies:
        print("Error creating companies")
        return
    created_routes = create_routes()
    if not created_routes:
        print("Error creating routes")
        return
    routes = [1, 2]
    for route_id in routes:
        created_buses = create_buses(route_id=route_id)
        if not created_buses:
            print(f"Error creating buses for route {route_id}")
            return
    print("Data filled successfully")


if __name__ == '__main__':
    main()
