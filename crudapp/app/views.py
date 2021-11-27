from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .serializer import studentSerializers
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
# Create your views here.

@csrf_exempt
def crud_app(request):
     if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = studentSerializers(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

     if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = studentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg ':'data inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

     if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = studentSerializers(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

     if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg' : "data Deleted"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')


# function based api view
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'this is get request','data':request.data})
    if request.method == 'POST':
        return Response({'msg' : 'this is post method','data':request.data})
