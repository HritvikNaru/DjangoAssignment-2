from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
class Employee(models.Model):
    Name= models.CharField(max_length=100)
    MobileNumber= models.CharField(max_length=50)
    Email= models.EmailField()
    Address= models.CharField(max_length=200)
    history = HistoricalRecords()

class Device(models.Model):
    Name= models.CharField(max_length=100)
    Type= models.CharField(max_length=100)
    Cost= models.IntegerField()
    Allocated=models.BooleanField(default=False)
    EmployeeAssigned=models.ForeignKey(Employee , on_delete=models.SET_DEFAULT,related_name="employee",null=True,default=None,blank=True)
    history = HistoricalRecords()

