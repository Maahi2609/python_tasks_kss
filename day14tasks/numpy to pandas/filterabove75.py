'''Two arrays:
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
Task:
● Create a DataFrame with columns "Name" and "Marks"
● Filter students with marks above 75'''

import pandas as pd
import numpy as np
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
S = pd.DataFrame({"Name" : names , "Marks" : marks})
print(S[marks > 75])