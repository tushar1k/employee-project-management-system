from django.contrib import admin
from .models import Employee,Project

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('Employee_id', 'Name', 'Designation' , 'Department', 'is_Active')

admin.site.register(Employee, EmployeeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Project_Name', 'Project_Manager','Status')

admin.site.register(Project, ProjectAdmin)