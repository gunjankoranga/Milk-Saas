USER AUTHENTICATION SYSTEM DOCUMENTATION
======================================

1. OVERVIEW
-----------
A production-ready REST API authentication system built with Django, featuring:
- Username/phone number authentication
- JWT token-based security
- Rate limiting
- Redis caching
- Failed login attempt protection
- Comprehensive error logging

2. API ENDPOINTS
---------------

2.1 REGISTRATION
Endpoint: /api/register/
Method: POST
Rate Limit: 20 requests/minute

Request Format:
{
    "username": "example_user",
    "phone_number": "+919876543210",
    "email": "user@example.com",  (optional)
    "password": "secure_password"
}

Success Response (201):
{
    "token": "<JWT_ACCESS_TOKEN>",
    "message": "Registration successful"
}

Error Response (400):
{
    "username": ["user with this username already exists."],
    "phone_number": ["user with this phone number already exists."]
}

2.2 LOGIN
Endpoint: /api/login/
Method: POST
Rate Limit: 20 requests/minute

Request Format:
{
    "login_field": "example_user",  (username or phone number)
    "password": "secure_password"
}

Success Response (200):
{
    "token": "<JWT_ACCESS_TOKEN>",
    "message": "Login successful"
}

Error Response (401):
{
    "error": "Invalid credentials"
}

3. SECURITY FEATURES
-------------------
3.1 Rate Limiting
    - Anonymous: 100 requests/day
    - Authenticated: 1000 requests/day
    - Registration: 20 requests/minute
    - Login: 20 requests/minute

3.2 Failed Login Protection
    - Max attempts: 5 within 5 minutes
    - Lockout duration: 5 minutes
    - Auto-reset after successful login

3.3 JWT Configuration
    - Token lifetime: 30 days
    - Algorithm: HS256
    - Auto-expiry enabled

4. REDIS CACHING
---------------
- Cache TTL: 15 minutes
- Connection timeout: 5 seconds
- Max connections: 1000
- Connection pool: 100
- Retry on timeout: Enabled

5. ERROR LOGGING
---------------
- Error log location: logs/django-errors.log
- Startup errors: logs/django-startup-errors.log
- Log format: {levelname} {asctime} {module} {process:d} {thread:d} {message}
- Log levels: ERROR, WARNING, INFO

6. USAGE EXAMPLES
----------------

6.1 Registration:
curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "testuser",
    "phone_number": "+919876543210",
    "email": "test@example.com",
    "password": "your_password123"
}'

6.2 Login:
curl -X POST http://localhost:8000/api/login/ \
-H "Content-Type: application/json" \
-d '{
    "login_field": "testuser",
    "password": "your_password123"
}'

6.3 Using JWT Token:
curl -H "Authorization: Bearer <your_token>" \
http://localhost:8000/api/protected-endpoint/

7. ERROR CODES
-------------
200 - Success
201 - Created (Registration successful)
400 - Bad Request
401 - Unauthorized
403 - Forbidden
429 - Too Many Requests
500 - Internal Server Error

