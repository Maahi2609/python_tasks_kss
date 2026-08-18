'''Scenario:
Scenario:
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
Task:
● Convert to DataFrame
● Filter students with marks > 50
● Plot bar chart only for filtered students
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]
data = pd.DataFrame({"Marks":marks, "Names":names})
data = data[marks > 50]
print(data)
plt.bar(data["Names"], data["Marks"])
plt.title('student stats')
plt.xlabel('marks')
plt.ylabel('names')
plt.show()
