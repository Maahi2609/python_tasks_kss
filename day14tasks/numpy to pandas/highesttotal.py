'''Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total
'''

import pandas as pd
import numpy as np
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
df = pd.DataFrame(arr, columns = ["Math", "Science"])
df["Total"] = df["Math"] + df["Science"]
print(df)
highest = df["Total"].idxmax()
print("student with highest total : ",highest)
print("highest total :",df["Total"].max())