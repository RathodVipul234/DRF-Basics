from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('StudentModelViewSet', StudentModelViewSet, basename='studentModel')

urlpatterns = [
    path('', include(router.urls)),
    # for login & logout btn in session authentication
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token)
]
