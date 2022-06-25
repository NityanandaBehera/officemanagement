from datetime import datetime
from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def view_all(request):
    emps = Employee.objects.all()
    return render(request, 'view.html', {'emps': emps})


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Employee(first_name=first_name, last_name=last_name,
                           salary=salary, bonus=bonus, role_id=role, dept_id=dept, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method == "GET":
        return render(request, 'add.html')
    else:
        return HttpResponse("An Exception occured! Employee")


def remove_emp(request):
    return render(request, 'remove.html')


def details_emp(request):
    return render(request, 'details.html')
# Create your views here.
