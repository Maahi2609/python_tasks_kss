'''A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy.'''

employees = [[101, "A"], [102, "B"], [103, "C"]]
employees_copy = employees.copy()
employees[0][1] = "Z"
print("original : ",employees)
print("Shallow Copy : ",employees_copy)

import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
employees_copy = copy.deepcopy(employees)
employees[0][1] = "Z"
print("original : ",employees)
print("Deep Copy : ",employees_copy)
