from django.shortcuts import render, get_object_or_404
from .models import Employee, Project
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    total_Employee = Employee.objects.count()
    active_employee = Employee.objects.filter(is_Active = True).count()
    total_project = Project.objects.count()
    completed_project = Project.objects.filter(Status = 'Completed').count()

    context= {
        'emp' : total_Employee,
        'active' : active_employee,
        'projects' : total_project,
        'completed' : completed_project,
    }

    return render(request,'home.html',context)

def list(request):
    employees = Employee.objects.all()

    department = request.GET.get('department')

    if department:
        employees = employees.filter(Department=department)

    paginator = Paginator(employees, 10)

    page_number = request.GET.get('page')

    employees = paginator.get_page(page_number)

    return render(request, 'list.html', {
        'employees': employees
    })

def projects(request):
    projects = Project.objects.all()

    paginator = Paginator(projects, 10)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    context = {
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def employee_detail(request, id):
    employee = get_object_or_404(
        Employee,
        Employee_id=id
    )

    projects = employee.projects.all()

    context = {
        'employee': employee,
        'projects': projects,
    }

    return render(request, 'employee_detail.html', context)

def project_detail(request, id):
    project = get_object_or_404(
        Project,
        id=id
        )
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)