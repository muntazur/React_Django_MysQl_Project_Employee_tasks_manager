from django.shortcuts import render
from .models import Employee,Task
from .serializers import EmployeeSerializer, TaskSerializer
from rest_framework import viewsets

# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
