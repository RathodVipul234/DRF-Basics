from django.shortcuts import render
from .models import Song, Singer
from .serializers import SingerSerializer, SonSerializer
from rest_framework import viewsets


# Create your views here.

class SonView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SonSerializer


class SingerView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
