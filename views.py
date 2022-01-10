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
from rest_framework.decorators import api_view #for function based view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class ListCreateStudent(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RetrieveUPdateDestroyStudent(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

