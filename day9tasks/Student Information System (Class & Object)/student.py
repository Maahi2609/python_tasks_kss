'''A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details.'''

class Student :
    def __init__(self, name, roll_number, marks):
        self.name = name 
        self.roll_number = roll_number 
        self.marks = marks 
    def display(self):
        print("name : ",self.name)
        print("roll_number : ",self.roll_number)
        print("marks : ",self.marks)
        print()
student1 = Student("Maahi", 23, 78)
student2 = Student("Aswini", 45, 88)
student3 = Student("Rohit", 31, 67)

student1.display()
student2.display()
student3.display()
