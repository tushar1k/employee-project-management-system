from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),

    path('employees/', views.list, name='list'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),

    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
]