'''Scenario:
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
Task:
● Convert into DataFrame
● Plot:
○ Line graph → salary trend
○ Bar chart → department-wise salary comparison
○ Pie chart → department distribution
○ Histogram → salary distribution
○ Scatter plot → index vs salary.'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
data = pd.DataFrame({"salaries":salaries, "departments":departments})
print(data)

plt.plot(data["departments"], data["salaries"])
plt.xlabel('departments')
plt.ylabel('salaries')
plt.title('salary trend')
plt.show()

plt.bar(data["departments"], data["salaries"])
plt.xlabel('departments')
plt.ylabel('salaries')
plt.title('Department-Wise Salary Comparison')
plt.show()

department_count = data["departments"].value_counts()
plt.pie(department_count,labels=department_count.index,autopct='%1.1f%%',startangle=90)
plt.xlabel('departments')
plt.ylabel('salaries')
plt.title('Department Distribution')
plt.show()

plt.hist(salaries, bins=4, histtype="bar")
plt.xlabel('salaries')
plt.ylabel('frequency')
plt.title('Salary Distribution')
plt.show()

department_index = np.arange(1, 7)
plt.scatter(department_index, salaries)
plt.xlabel('department_index')
plt.ylabel('salaries')
plt.title('Index vs Salary')
plt.show()