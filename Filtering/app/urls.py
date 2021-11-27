from django.urls import path
from .views import studentList

urlpatterns = [
    path('list/',studentList.as_view())
]
