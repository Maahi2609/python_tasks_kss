'''A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details.'''

class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee) :
        def display(self):
             print("Employee name : ",self.name)
             print("Salary : ",self.salary)

m = Manager("Naresh", 65000)
m.display()
                

