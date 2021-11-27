from django.shortcuts import render
from .serializer import studentModelSerilizer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


# Create your views here.

class studentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = studentModelSerilizer

    '''
    # For filter
        filterset_fields = ['city','passby']
        filter_backends = [DjangoFilterBackend]
    '''

    '''
    # For search
        filter_backends = [SearchFilter]
        search_fields = ['city']
        '^' start with search
        '=' exact search
        '@' full text search - currently only support postgres
        '$' Regex search 
        
        Ex:-
            search_fields = ['^name', ]   
    '''

    '''
    # Basic method
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby = user)
    '''

    '''
    # ordering
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    '''
