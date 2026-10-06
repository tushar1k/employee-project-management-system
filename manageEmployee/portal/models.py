from django.db import models

# Create your models here.
class Employee(models.Model):

    depatrment_choice = [
        ('IT', 'Information Technology'),
        ('FIN','Finance'),
        ('MKT', 'Marketing'), 
        ('HR' , 'Human Resource'),
    ]

    Employee_id = models.IntegerField(unique=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(null=True, blank=True, unique=True)
    Phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    Department = models.CharField(max_length=3, choices = depatrment_choice)
    Designation = models.CharField(max_length=30)
    Date_of_joining = models.DateField()
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_Active = models.BooleanField(default=True)

class Project(models.Model):

    project_status = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    Project_Name = models.CharField(max_length=100)
    Client_Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)

    Status = models.CharField(
        max_length=30,
        choices=project_status
    )

    Project_Manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_projects'
    )

    Start_Date = models.DateField(null=True, blank=True)
    End_Date = models.DateField(null=True, blank=True)

    Employees = models.ManyToManyField(
        Employee,
        related_name='projects'
    )


def __str__(self):
    return self.Name