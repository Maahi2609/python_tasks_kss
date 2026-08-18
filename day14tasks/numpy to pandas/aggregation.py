'''A dataset:
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
Task:
● Convert to DataFrame with columns "Sales", "Profit"
● Filter rows where Sales > 100
● Find average Profit of filtered rows.'''

import pandas as pd
import numpy as np
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
S = pd.DataFrame(arr, columns = ["Sales", "Profit"])
filter = S[S["Sales"] > 100]
print(filter)
print("average profit : ",filter["Profit"].mean())
