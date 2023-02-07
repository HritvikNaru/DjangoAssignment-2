from rest_framework import serializers
from .models import Employee,Device

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    FirstName= serializers.CharField(max_length=100)
    LastName= serializers.CharField(max_length=100)
    MobileNumber= serializers.CharField(max_length=50)
    Email= serializers.EmailField()
    Address= serializers.CharField(max_length=200)
    class Meta:
        model = Employee
        fields = (
            'FirstName',
            'LastName',
            'MobileNumber',
            'Email',
            'Address'
        )


class DeviceDetailsSerializer(serializers.ModelSerializer):
    Name= serializers.CharField(max_length=100)
    Type= serializers.CharField(max_length=100)
    Cost=serializers.IntegerField()
    
    class Meta:
        model = Device
        fields = (
            'id',
            'Name',
            'Type',
            'Cost',
            'EmployeeAssigned'  
        )