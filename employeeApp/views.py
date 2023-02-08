from .models import Employee,Device
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from . Thread import EmailThread
from .serializers import DeviceDetailsSerializer
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from faker import Faker
fake=Faker()
from faker.providers import phone_number
fake.add_provider(phone_number)

@method_decorator(csrf_exempt, name='dispatch')
class Employees(viewsets.ViewSet):
        
        def list(self,request):
                data=Employee.objects.all().values()
                return HttpResponse(data)  
       
        def post(self,request):
                post=Employee()
                post.Name= request.POST.get('name')
                # post.LastName = request.POST.get('Lname')
                post.MobileNumber= request.POST.get('Mobile')
                post.Email= request.POST.get('email')
                post.Address= request.POST.get('address')       
                post.save()
                return HttpResponse("done!!")  
        
        @action(detail=False, methods=['POST'], name='Type')
        def delete(self,request):
                did= request.POST.get('empid')
                print(did)
                Employee.objects.filter(id=did).delete()
                return HttpResponse("done!!")
        
        @action(detail=False, methods=['GET'], name='Type')
        def database(self,request):
                data=Employee.objects.all().values()
                return HttpResponse(data)  
        
        @action(detail=False, methods=['POST'], name='Type')
        def search(self,request):
                srch=request.POST.get("search")
                ret = Employee.objects.filter(Name__icontains=srch).values()
                return HttpResponse(ret)
        @action(detail=False, methods=['GET'], name='Type')
        def history(self,request):
                data=Employee.history.all().values()
                return HttpResponse(data) 
        
        @action(detail=False, methods=['POST'], name='Type')
        def mock(self,request):
                
                for i in range(10):
                        post=Employee()
                        post.Name= fake.name()
                        
                        post.MobileNumber= fake.phone_number()
                        post.Email= ""
                        post.Address= fake.address()       
                        post.save()
                        print(i,"done")
                return HttpResponse("Complete!!")  






@method_decorator(csrf_exempt, name='dispatch')
class Devices(viewsets.ViewSet):
        
        def list(self,request):
                
                query=Device.objects.all()
                serializer=DeviceDetailsSerializer(query,many=True)
                return Response(serializer.data)

        def post(self,request):
                post=Device()
                post.Name= request.POST.get('Dname')
                post.Type = request.POST.get('Dtype')
                post.Cost= request.POST.get('Dcost')
                post.Allocated= request.POST.get('Allocated')
                eid=request.POST.get('Eassigned')
                if eid != "":
                        post.EmployeeAssigned=Employee.objects.get(id=eid)
                post.save()
                return HttpResponse("done!!")  
        
        @action(detail=False, methods=['GET'], name='Type')
        def type(self,request):
                dtype=Device.objects.all().values("Type")
                print(type(dtype))
                return HttpResponse(dtype) 
        
        @action(detail=False, methods=['POST'], name='Type')
        def delete(self,request):
               
                did= request.POST.get('Deviceid')
                print(did)
                Device.objects.filter(id=did).delete()
                return HttpResponse("done!")
        
        @action(detail=False, methods=['GET'], name='Type')
        def database(self,request):
                data=Device.objects.all().values()
                return HttpResponse(data)  
        
        
        @action(detail=False, methods=['POST'], name='Type')
        def allocate(self,request):
                EmailThread().start()
                did= request.POST.get('Deviceid')
                eid=request.POST.get('empid')
                data=Device.objects.filter(id=did).update(EmployeeAssigned=eid,Allocated=True)
                return HttpResponse("done")
        
        @action(detail=False, methods=['POST'], name='Type')
        def deallocate(self,request):
                EmailThread().start()
                did= request.POST.get('Deviceid')
                data=Device.objects.filter(id=did).update(EmployeeAssigned=None,Allocated=False)
                return HttpResponse("done")
        

        @action(detail=False, methods=['POST'], name='Type')
        def switch(self,request):
                eid1= request.POST.get('empid1')
                eid2= request.POST.get('empid2')
                emp1=Device.objects.filter(id=eid1).values("EmployeeAssigned")[0]["EmployeeAssigned"]
                emp2=Device.objects.filter(id=eid2).values("EmployeeAssigned")[0]["EmployeeAssigned"]
                Device.objects.filter(id=eid1).update(EmployeeAssigned=emp2)
                Device.objects.filter(id=eid2).update(EmployeeAssigned=emp1)
                return HttpResponse("done")
        
        @action(detail=False, methods=['GET','POST'], name='Type')
        def search(self,request):
                srch=request.POST.get("search")
                ret = Device.objects.filter(Name__icontains=srch).values()
                return HttpResponse(ret)  

        @action(detail=False, methods=['GET'], name='Type')
        def history(self,request):
                data=Device.history.all().values()
                return HttpResponse(data) 



       
 