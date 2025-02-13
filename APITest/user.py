import requests

# API endpoints
BASE_URL = 'http://127.0.0.1:8000//api'
REGISTER_URL = f'{BASE_URL}/register/'
LOGIN_URL = f'{BASE_URL}/login/'

# Registration
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

# Login
def login_user(login_field, password):
    data = {
        "login_field": login_field,  # Can be username or phone number
        "password": password
    }
    response = requests.post(LOGIN_URL, json=data)
    print("Login Response:", response.json())
    return response.json()

# Example usage
if __name__ == "__main__":
    # Register new user
    register_response = register_user()
    
    # Login with username
    login_response = login_user("testuser", "Password123")
    
    # Login with phone number
    login_response = login_user("+919876543210", "Password123")