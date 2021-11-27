from django.urls import path
from .views import crud_app,hello_world
urlpatterns = [
    path('crud-app/', crud_app),
    ''' browsable api view ''',
    path('hello-world/', hello_world),
]
