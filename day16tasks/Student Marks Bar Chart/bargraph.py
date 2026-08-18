'''Scenario:
Marks of students:
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
Task:
● Create a DataFrame
● Plot a bar graph
● Show student names on X-axis.'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])
data = pd.DataFrame({"Name":names, "Marks":marks})
print(data)
plt.bar(names, marks)
plt.title('Student Info')
plt.xlabel('names')
plt.ylabel('marks')
plt.show()