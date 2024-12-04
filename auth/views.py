from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.db import transaction
from rest_framework import generics, permissions
from django.db import connection
from django.utils.crypto import get_random_string

from .serializers import UserSerializer
#---------------------------------Login---------------------------------
@api_view(['POST'])
def login(request):
    try:
        user = get_object_or_404(User, email=request.data['email'])
        if user.check_password(request.data['password']):
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({'token': token.key, 'user': serializer.data})
        else:
            return Response("Invalid credentials", status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response("User not found", status=status.HTTP_404_NOT_FOUND)
#---------------------------------Admin Login---------------------------------
@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token_key = request.headers.get('Authorization').split(' ')[1]
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response("Logout successful", status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response("Invalid token", status=status.HTTP_401_UNAUTHORIZED)
#---------------------------------Register---------------------------------  
