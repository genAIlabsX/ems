## Objective
Develop a simple Employee Management System using Spring Boot for the backend, H2 in-memory database for data storage, and HTML/CSS for the frontend.

## Requirements
1. Project Setup
    * Use Spring Boot (preferably with Spring Initializr).
    * Include dependencies:
        * Spring Web
        * Spring Data JPA
        * H2 Database
        * Thymeleaf (for HTML rendering)
2. Core Features
    * Add New Employee
        * A form to input employee details: Name, Email,        Department, and Salary.
        * On submission, the data should be saved to the H2 database.
    * View All Employees
        * A page that lists all employees in a tabular      format.
        * Data should be fetched from the H2 database and displayed using Thymeleaf.
3. Database
    * Use H2 in-memory database.
    * Configure the database in application.properties.
    * Enable the H2 console for debugging.
4. Frontend
    * Use HTML/CSS for UI.
    * Use Thymeleaf templates for rendering dynamic content.
    * Keep the UI simple and clean.

## Project Code Structure
employee-management
* src/
    * main/
        * java/com/example/employeemanagement/
            * controller/
            * model/
            * repository/
            * service/
        * resources/
            * templates/
                * add-employee.html
                * view-employees.html
            * application.properties
* pom.xml

## Additional
create README.md with:
* Project overview
* Setup instructions

