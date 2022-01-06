from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

def student_detail(request,pk):
    # stu=Student.objects.all()
    # serializer=StudentSerializer(stu,many=True)
    stu=Student.objects.get(id=pk)
    # print(stu)
    serializer=StudentSerializer(stu)
    # print(serializer)
    json_data=JSONRenderer().render(serializer.data)
    # print(json_data)
    # return JsonResponse(serializer.data,safe=False)
    return HttpResponse(json_data,content_type="application/json")

def student_list(request):
    try:
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        # json_data=JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
    except:
        print("LL")
        data = {}
        data['status'] = status.HTTP_400_BAD_REQUEST
        data['error'] = "something went wrong"
        return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        print(request.body)
        json_data=request.body
        stream=io.BytesIO(json_data) 
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            # res={'msg':'Data Created'}
            # json_data=JSONRenderer().render(res)
            return HttpResponse(serializer.data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
    
