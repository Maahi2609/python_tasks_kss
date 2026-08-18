'''Scenario:
A teacher stores student names and marks in a list of tuples.
Task:
● Convert data into a dictionary
● Use a loop + condition to find students scoring above 50
● Use math module to calculate average
● Store results in a text file
'''

import math

tu1 = ("Mahesh", "Aswini", "Jaggu", "Lachi")
tu2 = (89, 96, 67, 79)
d = dict(zip(tu1, tu2))
print(d)
print("\nStudents scoring above 50:")
for name, marks in d.items():
    if marks > 50:
        print(name, marks)

total = sum(tu2)
average = total / len(tu2)
print("\nAverage marks:", average)
with open("Student_results.txt", "w") as file:
    file.write("Student dictionary:\n")
    file.write(str(d))

    file.write("\n\nStudents scoring above 50:\n")

    for name, marks in d.items():
        if marks > 50:
            file.write(f"{name}: {marks}\n")
    file.write(f"\nAverage Marks: {math.floor(average * 100) / 100}")
print("\nResults saved to Student_results.txt")