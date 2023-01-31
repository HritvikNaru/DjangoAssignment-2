from rest_framework import serializers
from .models import EmployeeDetails,DeviceDetails

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    FirstName= serializers.CharField(max_length=100)
    LastName= serializers.CharField(max_length=100)
    MobileNumber= serializers.CharField(max_length=50)
    Email= serializers.EmailField()
    Address= serializers.CharField(max_length=200)
    class Meta:
        model = EmployeeDetails
        fields = (
            'FirstName',
            'LastName',
            'MobileNumber',
            'Email',
            'Address'
        )


class DeviceDetailsSerializer(serializers.ModelSerializer):
    DeviceName= serializers.CharField(max_length=100)
    DeviceType= serializers.CharField(max_length=100)
    DeviceCost=serializers.IntegerField()
    
    class Meta:
        model = DeviceDetails
        fields = (
            'DeviceName',
            'DeviceType',
            'DeviceCost'  
        )