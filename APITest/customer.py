import requests

BASE_URL = 'http://127.0.0.1:8000/api/collector'

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMDQwMzkxLCJpYXQiOjE3Mzk0NDgzOTEsImp0aSI6IjhkYzFjZDExYzRhNzQ4OTU5MGM3ZmViMjVlZTgxM2NlIiwidXNlcl9pZCI6Mn0.BoL5VCVm903Jq8GYLgz9D8PDOfBZlRtLsRbcVHmZ_z0"

headers = {
    "Authorization": f"Bearer {token}"
}


def create_customer():
    data = {
        "name": "customer 3",
        "phone": "+919876543210"
    }

    response = requests.post(f'{BASE_URL}/customers/', json=data, headers=headers)

    print(response.json())


def get_customers():
    response = requests.get(f'{BASE_URL}/customers/?page=1', headers=headers)
    print(response.json())


def get_customer(customer_id):
    response = requests.get(f'{BASE_URL}/customers/{customer_id}/', headers=headers)
    print(response.json())


def update_customer(customer_id):
    data = {
        "name": "customer 1 updated",
        "phone": "+919876543210"
    }
    response = requests.put(f'{BASE_URL}/customers/{customer_id}/', json=data, headers=headers)
    print(response.json())


def delete_customer(customer_id):
    response = requests.delete(f'{BASE_URL}/customers/{customer_id}/', headers=headers)
    print("Delete Customer Response:", response.status_code)
    print(response.json())
    
if __name__ == "__main__":
    create_customer()