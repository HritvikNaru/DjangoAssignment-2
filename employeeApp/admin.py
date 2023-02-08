from django.contrib import admin

from .models import Employee,Device
@admin.register(Employee)

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','Name','MobileNumber','Email','Address']

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display=['id','Name','Type','Cost','Allocated','EmployeeAssigned']
