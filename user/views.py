from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.core.cache import cache
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny
import logging

logger = logging.getLogger('user')
User = get_user_model()

class CustomAnonRateThrottle(AnonRateThrottle):
    rate = '20/minute'

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [CustomAnonRateThrottle]

    def post(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                token = RefreshToken.for_user(user)
                
                response_data = {
                    'token': str(token.access_token),
                    'message': 'Registration successful'
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            logger.warning(f"Validation error during registration: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Unexpected error during registration: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [CustomAnonRateThrottle]

    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                login_field = serializer.validated_data['login_field']
                password = serializer.validated_data['password']
                
                # Check failed login attempts
                cache_key = f"login_attempts_{login_field}"
                failed_attempts = cache.get(cache_key, 0)
                
                if failed_attempts >= 5:  # Lock after 5 failed attempts
                    return Response({
                        'error': 'Too many failed attempts. Please try again later.'
                    }, status=status.HTTP_429_TOO_MANY_REQUESTS)
                
                user = authenticate(request, username=login_field, password=password)
                
                if not user:
                    try:
                        user_obj = User.objects.get(phone_number=login_field)
                        user = authenticate(
                            request,
                            username=user_obj.username,
                            password=password
                        )
                    except User.DoesNotExist:
                        user = None

                if user:
                    if not user.is_active:
                        return Response({
                            'error': 'Account is disabled'
                        }, status=status.HTTP_403_FORBIDDEN)
                    
                    # Reset failed attempts on successful login
                    cache.delete(cache_key)
                    
                    token = RefreshToken.for_user(user)
                    return Response({
                        'token': str(token.access_token),
                        'message': 'Login successful',
                        'user': {
                            'username': user.username,
                            'phone_number': user.phone_number,
                            'email': user.email
                        }
                    }, status=status.HTTP_200_OK)
                
                # Increment failed attempts
                cache.set(cache_key, failed_attempts + 1, timeout=300)  # 5 minutes timeout
                
                return Response({
                    'error': 'Invalid credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            logger.error(f"Unexpected error during login: {str(e)}")
            return Response(
                {'error': 'An unexpected error occurred'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )