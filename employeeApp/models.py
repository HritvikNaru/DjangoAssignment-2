from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    FirstName= models.CharField(max_length=100)
    LastName= models.CharField(max_length=100)
    MobileNumber= models.CharField(max_length=50)
    Email= models.EmailField()
    Address= models.CharField(max_length=200)


class DeviceDetails(models.Model):
    DeviceName= models.CharField(max_length=100)
    DeviceType= models.CharField(max_length=100)
    DeviceCost= models.IntegerField()
    

class DeviceRights(models.Model):
    Employee=models.ForeignKey(EmployeeDetails , on_delete=models.CASCADE)
    Device=models.ForeignKey(DeviceDetails, on_delete=models.CASCADE)
