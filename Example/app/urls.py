from .views import student,create_student,update_student
from django.urls import path

urlpatterns = [
    path('',student),
    path('create/',create_student),
    path('update/',update_student)
]
