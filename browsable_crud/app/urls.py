from django.urls import path, include
from .views import student_api, StudentAPI, StudentList, StudentCreate, \
    StudentSingleRetrieve, StudentUpdate, StudentDelete, \
    MixingCrud, MixingCrudPK, StudentListConcrete, \
    StudentUpdateConcrete, StudentCreateConcrete, \
    StudentRetrieveConcrete, StudentViewSet, StudentModelViewSet, third_party_crud_app

# routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('StudentViewSet', StudentViewSet, basename='student')
router.register('StudentModelViewSet', StudentModelViewSet, basename='studentModel')

urlpatterns = [
    path('student-api/', student_api),
    path('student-api/<int:id>/', student_api),

    # class based view

    path('student-api-classBased/', StudentAPI.as_view()),
    path('student-api-classBased/<int:id>/', StudentAPI.as_view()),

    # particular mixing view

    path('student-api-StudentList/', StudentList.as_view()),
    path('student-api-Student-id/<int:pk>/', StudentSingleRetrieve.as_view()),
    path('student-api-Student-create/', StudentCreate.as_view()),
    path('student-api-Student-update/<int:pk>/', StudentUpdate.as_view()),
    path('student-api-Student-delete/<int:pk>/', StudentDelete.as_view()),

    # all in one mixing view

    path('student-mixing-crud/<int:pk>/', MixingCrudPK.as_view()),
    path('student-mixing-crud/', MixingCrud.as_view()),

    # concrete class view

    path('StudentListConcrete/', StudentListConcrete.as_view()),
    path('StudentCreateConcrete/', StudentCreateConcrete.as_view()),
    path('StudentRetrieveConcrete/<int:pk>/', StudentRetrieveConcrete.as_view()),
    path('StudentUpdateConcrete/<int:pk>/', StudentUpdateConcrete.as_view()),

    # ViewSet

    path('', include(router.urls)),

    # third party app

    path('third_party_crud_app/', third_party_crud_app)

]
