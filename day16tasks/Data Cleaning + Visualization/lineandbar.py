'''Scenario:
data = np.array([100, np.nan, 200, 150, np.nan, 300])
Task:
1. Convert to Pandas Series
2. Replace NaN with mean
3. Plot:
○ Line graph of cleaned data
○ Bar chart of values > average.'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = np.array([100, np.nan, 200, 150, np.nan, 300])
S = pd.Series(data)
mean = S.mean()
S = S.fillna(mean)
print(S)
plt.plot(S)
plt.title('Cleaned Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
average = S.mean()
filtered = S[S > average]
plt.bar(filtered.index, filtered.values)
plt.title('Values Greater Than Average')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()