from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('StudentModelViewSet', StudentModelViewSet, basename='studentModel')

urlpatterns = [
    path('', include(router.urls)),
    path('get-token/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('verify-token/', TokenVerifyView.as_view()),

]
'''

     1.generate token
     http POST http://127.0.0.1:8001/get-token/ username="admin" password="admin"
     
     2.verify token
     http POST http://127.0.0.1:8001/verify-token/ token="<access token>"
     
     3.refresh token
     http POST http://127.0.0.1:8001/refresh-token/ refresh="<refresh token>"

    Note :- access token expired in every 5 minute     
         -> generate new token after every 5 minute using step 3
         
    How to Use It:-
    http GET http://127.0.0.1:8001/StudentModelViewSet/ "Authorization:Bearer <access token>"
    

          
'''
