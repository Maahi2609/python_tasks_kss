'''A dataset:
arr = np.array([10, 25, 30, 15, 40])
Task:
● Convert to Pandas Series
● Filter values greater than 20'''

import pandas as pd
import numpy as np
arr = np.array([10, 25, 30, 15, 40])
data = pd.Series(arr)
print(data[data > 20])