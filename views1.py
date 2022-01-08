from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt # for function based view
from rest_framework.response import Response
from rest_framework import exceptions, status
import json
# from django.utils.decorators import method_decorator 
from django.utils.decorators import method_decorator#for class based view
from django.views import View # for class based view
from rest_framework.views import APIView

# @method_decorator(csrf_exempt,name="dispath")
# @method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(APIView):
    def get(self, request,*args, **kwargs):
        try: 
            json_data=request.data
            print(json_data)
            print(json_data,"<<<<<<<<<<<<<<<<<<<<<<<<<<")
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            print(pythondata)

            id=pythondata.get('id',None)

            print(type(id))
            if id is not None:
                print("yes id printed")
                stu=Student.objects.filter(id=id).first()
                serializer=StudentSerializer(stu)
                return JsonResponse(serializer.data,content_type="application/json")
        except:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            # json_data=JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data,content_type="application/json")
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)

    def post(self, request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_200_OK
            res['msg']="Data Created Successfully......"
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type="application/json")
            return JsonResponse(res)#,status=status.HTTP_400_BAD_REQUEST)
        
        # json_data=JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data,content_type="application/json")
        # return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request,*args, **kwargs):
        json_data=request.body #json data
        stream=io.BytesIO(json_data)  #de-serialize
        pythondata=JSONParser().parse(stream)  #de-serialize
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)#complex data
        if serializer.is_valid():
            serializer.save()
            res={}
            res['status'] = status.HTTP_200_OK
            res['msg']="Data Updated Successfully......"
            return JsonResponse(res)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,*args, **kwargs):
         #json data
        # json_data=request.body
        # stream=io.BytesIO(json_data)  #de-serialize
        # pythondata=JSONParser().parse(stream)  #de-serialize
        data=request.data
        id=data.get('id')
        stu=Student.objects.filter(id=id).first()
        print(stu,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        stu.delete()
        print("Data Deleted Successfully.........")
        res={}
        res["msg"]="data deleted"
        res["status"]=status.HTTP_200_OK
        return Response(res,safe=False)
    
    
    
# def student_detail(request,pk):
#     # stu=Student.objects.all()
#     # serializer=StudentSerializer(stu,many=True)
#     stu=Student.objects.get(id=pk)
#     # print(stu)
#     serializer=StudentSerializer(stu)
#     # print(serializer)
#     json_data=JSONRenderer().render(serializer.data)
#     # print(json_data)
#     # return JsonResponse(serializer.data,safe=False)
#     return HttpResponse(json_data,content_type="application/json")

# def student_list(request):
#     try:
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         # json_data=JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data,content_type="application/json")
#         return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
#     except:
#         print("LL")
#         data = {}
#         data['status'] = status.HTTP_400_BAD_REQUEST
#         data['error'] = "something went wrong"
#         return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def student_create(request):
#     if request.method == "POST":
#         print(request.body)
#         json_data=request.body
#         stream=io.BytesIO(json_data) 
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)   
#         if serializer.is_valid():
#             serializer.save()
#             # res={'msg':'Data Created'}
#             # json_data=JSONRenderer().render(res)
#             return JsonResponse(serializer.data,content_type="application/json")
#         json_data=JSONRenderer().render(serializer.errors)
#         data = {}
#         data['status'] = status.HTTP_400_BAD_REQUEST
#         data['error'] = "something went wrong"
#         return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         print(pythondata)
      
#         id=pythondata.get('id',None)

#         print(type(id))
#         if id is not None:
#             print("yes id printed")
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data,content_type="application/json")

#         print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         # json_data=JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data,content_type="application/json")
#         return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
#     if request.method =="POST":
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={}
#             res['status'] = status.HTTP_200_OK
#             res['msg']="Data Created Successfully......"
#             # json_data=JSONRenderer().render(res)
#             # return HttpResponse(json_data,content_type="application/json")
#             return JsonResponse(res)#,status=status.HTTP_400_BAD_REQUEST)
        
#         # json_data=JSONRenderer().render(serializer.errors)
#         # return HttpResponse(json_data,content_type="application/json")
#         # return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
         
#     if request.method == "PUT":
#         json_data=request.body #json data
#         stream=io.BytesIO(json_data)  #de-serialize
#         pythondata=JSONParser().parse(stream)  #de-serialize
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=pythondata,partial=True) #complex data
#         if serializer.is_valid():
#             serializer.save()
#             res={}
#             res['status'] = status.HTTP_200_OK
#             res['msg']="Data Updated Successfully......"
#             return JsonResponse(res)
#         return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         json_data=request.body #json data
#         stream=io.BytesIO(json_data)  #de-serialize
#         pythondata=JSONParser().parse(stream)  #de-serialize
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={}
#         res["msg"]="data deleted"
#         res["status"]=status.HTTP_200_OK
#         return JsonResponse(res,safe=False)
    
        
