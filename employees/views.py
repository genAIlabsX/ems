import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm

def home(request):
    """
    View function for the home page.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered home page
    """
    return render(request, 'employees/home.html')

def department_list(request):
    """
    View function to display list of departments.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered department list page
    """
    departments = Department.objects.all()
    return render(request, 'employees/department_list.html', {'departments': departments})

def department_create(request):
    """
    View function to create a new department.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered department creation form or redirect to department list
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully!')
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'employees/department_form.html', {'form': form})

def department_update(request, pk):
    """
    View function to update a department.
    
    Args:
        request: HTTP request object
        pk: Primary key of department to update
        
    Returns:
        HttpResponse: Rendered department update form or redirect to department list
    """
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully!')
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'employees/department_form.html', {'form': form, 'department': department})

def department_delete(request, pk):
    """
    View function to delete a department.
    
    Args:
        request: HTTP request object
        pk: Primary key of department to delete
        
    Returns:
        HttpResponse: Redirect to department list
    """
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully!')
        return redirect('department_list')
    return render(request, 'employees/department_confirm_delete.html', {'department': department})

def employee_list(request):
    """
    View function to display list of employees with search/filter functionality.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered employee list page
    """
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    department_filter = request.GET.get('department', '')
    
    employees = Employee.objects.all()
    
    # Apply search filter
    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__name__icontains=query)
        )
    
    # Apply status filter
    if status_filter:
        status_bool = status_filter == 'Active'
        employees = employees.filter(status=status_bool)
    
    # Apply department filter
    if department_filter:
        employees = employees.filter(department__name=department_filter)
    
    departments = Department.objects.all()
    
    context = {
        'employees': employees, 
        'departments': departments,
        'query': query,
        'status_filter': status_filter,
        'department_filter': department_filter
    }
    
    return render(request, 'employees/employee_list.html', context)

def employee_create(request):
    """
    View function to create a new employee.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered employee creation form or redirect to employee list
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/employee_form.html', {'form': form})

def employee_update(request, pk):
    """
    View function to update an employee.
    
    Args:
        request: HTTP request object
        pk: Primary key of employee to update
        
    Returns:
        HttpResponse: Rendered employee update form or redirect to employee list
    """
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'employees/employee_form.html', {'form': form, 'employee': employee})

def employee_delete(request, pk):
    """
    View function to delete an employee.
    
    Args:
        request: HTTP request object
        pk: Primary key of employee to delete
        
    Returns:
        HttpResponse: Redirect to employee list
    """
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')
    
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def export_employees_csv(request):
    """
    View function to export employee data to CSV.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: CSV file download response
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Department', 'Salary', 'Status'])
    
    employees = Employee.objects.all().values_list(
        'name', 'email', 'department__name', 'salary', 'status'
    )
    
    for employee in employees:
        # Convert status boolean to Active/Inactive string
        status_str = 'Active' if employee[4] else 'Inactive'
        writer.writerow([employee[0], employee[1], employee[2], employee[3], status_str])
    
    return response
