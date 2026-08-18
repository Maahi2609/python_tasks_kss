'''Scenario:
A school records marks of students in one subject:
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
Task:
● Convert to Pandas DataFrame
● Plot:
○ Line graph → trend of marks
○ Bar chart → student vs marks
○ Pie chart → Pass (>50) vs Fail
○ Histogram → distribution of marks
○ Scatter plot → index vs marks
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
data = pd.DataFrame({"marks":marks, "students":students})
print(data)

plt.plot(data['students'], data['marks'])
plt.title('Trend of Marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()


plt.bar(data['students'], data['marks'])
plt.title('students vs marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

pass_data = data[marks > 50]
print("Pass")
print(pass_data)

fail_data = data[marks <= 50]
print("Fail")
print(fail_data)

pass_count = len(pass_data)
fail_count = len(fail_data)

plt.pie([pass_count, fail_count], labels = ["Pass", "Fail"], autopct = '%1.1f%%', startangle=90)
plt.title('Pass (>50) vs Fail')
plt.xlabel('Pass_count')
plt.ylabel('Fail_count')
plt.show()

plt.hist(marks, bins=6, histtype="bar")
plt.title('Distribution Of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

students_index = np.arange(1, 8)
plt.scatter(students_index, marks)
plt.title('Index vs Marks')
plt.xlabel('Students_Index')
plt.ylabel('Marks')
plt.show()