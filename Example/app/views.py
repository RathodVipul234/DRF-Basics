from django.shortcuts import render, HttpResponse
from .models import Student
from .seriealizers import studentSerializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def student(request):
    obj = Student.objects.get(id=1)
    obj1 = Student.objects.all()
    print(obj)
    serializer = studentSerializers(obj)
    serializer1 = studentSerializers(obj1, many=True)
    json_data = JSONRenderer().render(serializer1.data)
    # import pdb;pdb.set_trace()
    return HttpResponse(json_data, content_type='application/json')
    # return render(request,'home.html',{'data':json_data})


@csrf_exempt
def create_student(request):
    if request.method == "POST":
        import pdb;
        pdb.set_trace()
        ''' Json data to python data '''
        json_data = request.body
        stream = io.update_studentBytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = studentSerializers(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    return HttpResponse("ok")


def update_student(request):
    # import pdb;pdb.set_trace()

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
            res = {'msg':'data updated'}
            json_data = JSONRenderer().render(res)
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



