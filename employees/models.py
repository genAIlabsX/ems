from django.db import models

class Department(models.Model):
    """
    Model representing a department within the organization.
    
    Attributes:
        name (str): The name of the department.
    """
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    """
    Model representing an employee within the organization.
    
    Attributes:
        name (str): The name of the employee.
        email (str): The email address of the employee.
        department (Department): The department the employee belongs to.
        salary (float): The salary of the employee.
        status (bool): Whether the employee is active or inactive.
    """
    STATUS_CHOICES = (
        (True, 'Active'),
        (False, 'Inactive'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name
