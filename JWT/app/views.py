from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import studentModelSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # globally set authentication in setting.py file
