from django import forms
from .models import Employee, Department

class DepartmentForm(forms.ModelForm):
    """
    Form for creating and updating Department objects.
    """
    class Meta:
        model = Department
        fields = ['name']
        
    def clean_name(self):
        """
        Validate that department name is not empty.
        
        Returns:
            str: Cleaned department name
        """
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Department name cannot be empty")
        return name

class EmployeeForm(forms.ModelForm):
    """
    Form for creating and updating Employee objects.
    """
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'salary', 'status']
        
    def clean_name(self):
        """
        Validate that employee name is not empty.
        
        Returns:
            str: Cleaned employee name
        """
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Employee name cannot be empty")
        return name
        
    def clean_email(self):
        """
        Validate employee email format.
        
        Returns:
            str: Cleaned email address
        """
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email cannot be empty")
        return email
        
    def clean_salary(self):
        """
        Validate employee salary is a positive number.
        
        Returns:
            decimal: Cleaned salary value
        """
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 0:
            raise forms.ValidationError("Salary cannot be negative")
        return salary
