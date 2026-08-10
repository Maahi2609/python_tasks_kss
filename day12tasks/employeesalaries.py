'''Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition.'''

import numpy as np
salaries = np.array([25000, 40000, 15000, 50000, 30000])
filter_salaries = salaries[salaries > 30000]
print("salaries above 30000 : ",filter_salaries)
count = np.sum(salaries > 30000)
print("num of employees : ",count)

