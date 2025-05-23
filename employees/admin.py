from django.contrib import admin
from .models import Employee, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Admin configuration for Department model.
    """
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Employee model.
    """
    list_display = ('name', 'email', 'department', 'salary', 'status')
    list_filter = ('status', 'department')
    search_fields = ('name', 'email')
