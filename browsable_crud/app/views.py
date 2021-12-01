from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import studentModelSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'], )
def student_api(request, id=None):
    if request.method == "GET":
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentModelSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = studentModelSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = studentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': " data Submitted"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        stu = Student.objects.get(id=id)
        serializer = studentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "completely data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        stu = Student.objects.get(id=id)
        serializer = studentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "partially data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data deleted '}, status=status.HTTP_200_OK)


# class based view
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentModelSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = studentModelSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = studentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': " data Submitted"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        stu = Student.objects.get(id=id)
        serializer = studentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "completely data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        stu = Student.objects.get(id=id)
        serializer = studentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "partially data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'data deleted '}, status=status.HTTP_200_OK)


# mixing views

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, CreateModelMixin, \
    UpdateModelMixin


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def get(self, request, id=None, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentSingleRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# all in one class
# no required pk
class MixingCrud(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# required pk
class MixingCrudPK(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


''' Concrete View Class'''
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView


class StudentListConcrete(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer


class StudentCreateConcrete(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer


class StudentRetrieveConcrete(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer


class StudentUpdateConcrete(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer


''' 
    as you see all code same only changes view class,
    listed bellow few more classes
    DestroyAPIView - delete object,
    ListCreateAPIView - create and show all objects,
    RetrieveUpdateAPIView - retrieve and update specific object,
    RetrieveDestroyAPIView - retrieve and destroy specific object,
    RetrieveUpdateDestroyAPIView - retrieve, update and destroy specific object,
    
'''

# viewSet

from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = studentModelSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer = studentModelSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = studentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': " data Submitted"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer = studentModelSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "completely data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        stu = Student.objects.get(id=pk)
        serializer = studentModelSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "partially data updated"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'data deleted '}, status=status.HTTP_200_OK)


# model view set
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentModelSerializer


''' crud with third party app'''
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def third_party_crud_app(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentModelSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = studentModelSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = studentModelSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg ': 'data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = studentModelSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': "data Deleted"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
