'''A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario:
She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected.'''

marks = [50, 60, 70, 80]
marks[0] = 25
backup = marks
print("marks : ",marks)
print("backup : ",backup)