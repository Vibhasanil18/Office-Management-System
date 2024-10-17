from django.shortcuts import render,HttpResponse
from django.views import View
from empapp.models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render (request,'index.html')

def allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render (request,'allemp.html',context) 
def addemp(request):
    if request.method ==  'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])



        new_emp = Employee(first_name = first_name, last_name = last_name, 
                           salary = salary,bonus = bonus, phone = phone,
                           dept_id = dept,role_id =role,
                           hire_date = datetime.now())
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    
    elif request.method=='GET':
        return render (request,'addemp.html')
    else :
        return HttpResponse("An Exception Occured!Employee has not been added")
 


def removeemp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("please Enter a valid Emp ID")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render (request,'removeemp.html',context)

def filteremp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        if role:
            emps = emps.filter(role__name__icontains = role)


        context = {
            'emps' : emps
        }
        return render(request, 'allemp.html',context)
    
    elif request.method == 'GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse("An Exception Occured")


