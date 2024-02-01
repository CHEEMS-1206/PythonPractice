from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    company_about = models.TextField()
    company_type = models.CharField(max_length=50, choices=(
        ('IT','IT'),("Non IT", "Non IT")
    ))
    company_added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name

# Emplyees model
class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=100)
    employee_address = models.CharField(max_length=200)
    employee_phone = models.CharField(max_length=10)
    employee_about = models.TextField()
    employee_position = models.CharField(max_length=50, choices=(
        ('Manager','Manager'),("depthead","Department Head"), ("sftengnr","Software Engineer")
    ))

    employee_company = models.ForeignKey(Company,on_delete=models.CASCADE)
