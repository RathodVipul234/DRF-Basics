from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import studentModelSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import VipulRateThrottle

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [AnonRateThrottle,VipulRateThrottle]
