from django.contrib import admin

from .models import EmployeeDetails,DeviceDetails
@admin.register(EmployeeDetails)

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','MobileNumber','Email','Address']

# Register your models here.
@admin.register(DeviceDetails)
class DeviceAdmin(admin.ModelAdmin):
    list_display=['id','DeviceName','DeviceType','DeviceCost']
