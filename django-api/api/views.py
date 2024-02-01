from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #custom endpoints

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None) :
        requestedCompany = Company.objects.get(pk=pk)
        requestedEmployees = Employee.objects.filter(employee_company = requestedCompany)
        # serialize the employees
        emps_serializer = EmployeeSerializer(requestedEmployees,many=True,context={"request":request})

        return Response(emps_serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer