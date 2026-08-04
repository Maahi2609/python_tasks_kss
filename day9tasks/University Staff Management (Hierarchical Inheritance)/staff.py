'''A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information.'''

class Staff :
    def __init__(self, name, age, dprtment):
        self.name = name
        self.age = age
        self.dprtment = dprtment

class Professor(Staff) :
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("dprtment : ",self.dprtment)

class LabAssistant(Staff) :
    def display(self):
        print("name : ",self.name)   
        print("age : ",self.age)
        print("dprtment : ",self.dprtment)

class Administrator(Staff) :
    def display(self):
        print("name : ",self.name)   
        print("age : ",self.age)
        print("dprtment : ",self.dprtment)

professor = Professor("Mahesh Babu",23 , "CSE")
labassistant = LabAssistant("Jaggu", 25, "ECE")
administrator = Administrator("Ravi", 39, "MECH")

print("Professor Details")
professor.display()

print("\nLab Assistant Details")
labassistant.display()

print("\nAdministrator Details")
administrator.display()