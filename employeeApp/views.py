from django.shortcuts import render,redirect
from .models import EmployeeDetails,DeviceDetails,DeviceRights
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
@csrf_exempt

# Create your views here.
# class EmployeeDetails(View):
    # def get(self,request):
    #     return render(request,"coursetemplates/register.html")
    
def Employee(request):
        post=EmployeeDetails()
        post.FirstName= request.POST.get('Fname')
        post.LastName = request.POST.get('Lname')
        post.MobileNumber= request.POST.get('Mobile')
        post.Email= request.POST.get('email')
        post.Address= request.POST.get('address')

        post.save()
                
        return HttpResponse("done!!")  


@csrf_exempt

def Devices(request):
        post=DeviceDetails()
        post.DeviceName= request.POST.get('Dname')
        post.DeviceType = request.POST.get('Dtype')
        post.DeviceCost= request.POST.get('Dcost')

        post.save()
                
        return HttpResponse("done!!")  


def DeviceType(request):
        dtype=DeviceDetails.objects.all().values("DeviceType")
        print(type(dtype))
        return HttpResponse(dtype)  

@csrf_exempt
def Devicepermission(request):
        send_mail(
                'Device Allocated',
                'The Device has been Allocated',
                'hritvik@attentive.ai',
                ['hritvik10@gmail.com'],
                fail_silently=False,
        )
        post=DeviceRights()
        did= request.POST.get('Deviceid')
        eid=request.POST.get('Employeeid')
        post.Device= DeviceDetails.objects.get(id=did)
        post.Employee = EmployeeDetails.objects.get(id=eid)

        post.save()
                
        return HttpResponse("done!!")  

@csrf_exempt
def DeviceDeallocate(request):
        send_mail(
                'Device Deallocated',
                'The Device has been deallocated',
                'hritvik@attentive.ai',
                ['hritvik10@gmail.com'],
                fail_silently=False,
        )
        did= request.POST.get('Deviceid')
        eid=request.POST.get('Employeeid')
        DeviceRights.objects.filter(Device=did, Employee=eid).delete()

        
                
        return HttpResponse("done!!")  


@csrf_exempt
def DevInfo(request):
        dtype= request.POST.get("Dtype")
        print("devtype::",dtype)
        devid=DeviceDetails.objects.filter(DeviceType=dtype).values("id")
        print("devid::",devid[0]['id'])
        empid=DeviceRights.objects.filter(Device=devid[0]['id']).values("Employee_id")
        print("empid::",empid[0]['Employee_id'])
        empname=EmployeeDetails.objects.filter(id=empid[0]['Employee_id']).values()
        print(empname)
        return HttpResponse("done!!")  

@csrf_exempt
def DeviceDel(request):
        
        send_mail(
                'Subject here',
                'Here is the message.',
                'hritvik@attentive.ai',
                ['hritvik10@gmail.com'],
                fail_silently=False,
        )
        did= request.POST.get('Deviceid')
        print(did)
        DeviceDetails.objects.filter(id=did).delete()

        

        return HttpResponse("done!!")  

@csrf_exempt
def EmployeeDel(request):
        
        did= request.POST.get('empid')
        print(did)
        EmployeeDetails.objects.filter(id=did).delete()
        return HttpResponse("done!!")  




@csrf_exempt
def EmployeeData(request):
        
        data=EmployeeDetails.objects.all().values()

        return HttpResponse(data)  


@csrf_exempt
def DeviceData(request):
        
        data=DeviceDetails.objects.all().values()

        return HttpResponse(data)  

@csrf_exempt
def SearchEmployee(request):
        srch=request.POST.get("search")
        ret = EmployeeDetails.objects.filter(FirstName__icontains=srch).values()

        return HttpResponse(ret)  


