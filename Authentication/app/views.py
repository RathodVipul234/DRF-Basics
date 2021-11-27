from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import studentModelSerializer

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # globally set authentication in setting.py file

    '''
        Basic Authentication
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]
        permission_classes = [AllowAny]
        permission_classes = [IsAdminUser]
    '''
    '''
        Session Authentication
        authentication_classes = [SessionAuthentication]
        permission_classes = [IsAuthenticated]
        permission_classes = [AllowAny]
        permission_classes = [IsAdminUser]
        permission_classes = [IsAuthenticatedOrReadOnly] -> authenticated user all permission and unauthenticated user only read permission

    '''

    '''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    how to access token api -->  http GET http://127.0.0.1:8000/StudentModelViewSet/ 'Authorization:Token 41f0e9d45cc0c7690ce5f71b49d9d3cdeb5301a7
    
    * How to generate Token
    1.Using admin panel
    2.using cmd
        -->python manage.py drf_create_token <username>
    3.By exposing an Api end point
        -->create auth.py file and write class
        
    4.using signal
    '''
