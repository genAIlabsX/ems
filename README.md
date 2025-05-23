# Employee Management System

A Python-based Employee Management System built with Django framework that allows users to add, view, update, and delete employee records.

## Project Overview

This Employee Management System provides a user-friendly interface to manage employee records, with the following features:

- Add new employees with details like Name, Email, Department, Salary, and Status
- View all employees in a tabular format
- Update existing employee details
- Delete employees
- Search/Filter functionality by name, department, or status
- Export employee data to CSV format
- Mark employees as Active/Inactive
- Input validation and error handling
- Department management (Add, View, Update, Delete)

## Setup Instructions

### Prerequisites

- Python
- pip (Python package manager)

### Installation

1. Clone the repository

2. Navigate to the project folder
   ```
   cd ems
   ```

3. Create a virtual environment
   ```
   python -m venv venv-ems
   ```

4. Activate the virtual environment
   - On Windows:
     ```
     .\venv-ems\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv-ems/bin/activate
     ```

5. Install the required packages
   ```
   pip install django
   ```

6. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Create a superuser (optional)
   ```
   python manage.py createsuperuser
   ```

8. Start the development server
   ```
   python manage.py runserver
   ```

9. Access the application at `http://127.0.0.1:8000/`

## Database Structure

The application uses SQLite database with the following structure:

### Employee Table
- name (String)
- email (String, unique)
- department (Foreign Key to Department)
- salary (Decimal)
- status (Boolean: Active/Inactive)

### Department Table
- name (String, unique)