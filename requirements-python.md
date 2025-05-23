## Objective
Create a Python-based Employee Management System using Django framework that allows users to add, view, update, and delete employee records. The system should store data persistently using database

## Requirements
1. Project setup
    * use Python
    * create dedicated python virtual environment named venvEMS and use to for all installing dependencies
    * use Django
2. Core Features
    * Add New Employee
        * A form to input employee details: Name, Email, Department, Salary, Status.
        * On submission, the data should be saved to the database.
    * View All Employees
        * A page that lists all employees in a tabular format.
        * Data should be fetched from database and displayed using 
    * Update Employee
        * Modify existing employee details
    * Delete Employee
        * Remove an employee 
3. Database
    * Use SQLite database
4. Frontend
    * Keep the UI simple and clean
    * make UI with nice look and feel, not bare-bones 
5. Required Enhancements\
These enhancements are mandatory:
    * Search/Filter Functionality (by name, department, or status)
    * Input Validation and Error Handling
    * Mark Employee as Active/Inactive
    * Export to CSV

## Project Code Structure
according to standard Django code structure

## Database structure
Tables:
* employee
    * name, 
    * email, 
    * department (foreign key)
    * salary
    * status [Active/Inactive]
* department
    * name

## Additional
create README.md with:
* Project overview
* Setup instructions

