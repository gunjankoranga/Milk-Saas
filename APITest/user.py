import requests

# API endpoints
BASE_URL = 'http://127.0.0.1:8000/api'
REGISTER_URL = f'{BASE_URL}/register/'
LOGIN_URL = f'{BASE_URL}/login/'

def register_user():
    data = {
        "username": "testuser",
        "phone_number": "+919876543210",
        "email": "test@example.com",
        "password": "Password123"
    }
    response = requests.post(REGISTER_URL, json=data)
    print("Registration Response:", response.json())
    return response.json()

def login_user(login_field, password):
    data = {
        "login_field": login_field,  # Can be username or phone number
        "password": password
    }
    response = requests.post(LOGIN_URL, json=data)
    print("Login Response:", response.json())
    return response.json().get('token')

def test_auth_flow():
    # Register new user
    register_response = register_user()
    
    # Login with username
    token = login_user("testuser", "Password123")

    # Login with phone number
    token = login_user("+919876543210", "Password123")
    
    return token

if __name__ == "__main__":
    test_auth_flow()