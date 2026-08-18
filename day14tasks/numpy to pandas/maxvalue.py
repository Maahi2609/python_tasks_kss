'''A dataset:
arr = np.array([12, 45, 22, 67, 34])
Task:
● Convert to Pandas Series
● Find the maximum value
'''

import pandas as pd
import numpy as np
arr = np.array([12, 45, 22, 67, 34])
data = pd.Series(arr)
print(data.max())