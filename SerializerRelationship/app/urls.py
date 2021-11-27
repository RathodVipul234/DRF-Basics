from django.urls import path,include
from .views import SonView, SingerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', SingerView, basename='singer')
router.register('song', SonView, basename='song')
# from .views import StudentList
urlpatterns = [
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls')),
]
