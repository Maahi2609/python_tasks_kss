'''A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data
'''

import pandas as pd
import numpy as np
arr = np.array([10, np.nan, 30, np.nan, 50])
data = pd.Series(arr)
arr = data.mean()
print(arr)
updated_data = data.fillna(arr)
print(updated_data)