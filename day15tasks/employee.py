'''5. Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees.'''

class Employee :
    class Employee:
     def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print()
employees = {}
try:
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print("\nEnter employee details")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        try:
            salary = float(input("Enter Salary: "))
            if salary < 0:
                raise ValueError("Salary cannot be negative")
            employee = Employee(emp_id, name, salary)
            employees[emp_id] = employee
        except ValueError:
            print("Invalid salary! Please enter a valid positive number.")
    print("\n--- Employee Details ---")
    for emp_id, employee in employees.items():
        employee.display()
    with open("employees.txt", "w") as file:
        for emp_id, employee in employees.items():
            file.write(
                f"ID: {employee.emp_id}, "
                f"Name: {employee.name}, "
                f"Salary: {employee.salary}\n"
            )
    print("Employee data saved successfully.")
except ValueError:
    print("Invalid number of employees.")
except Exception as e:
    print("An error occurred:", e)