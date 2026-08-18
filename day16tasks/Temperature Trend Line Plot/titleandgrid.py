'''Scenario:
Daily temperatures:
temps = np.array([28, 30, 32, 31, 29])
Task:
● Convert into Pandas Series
● Plot a line graph
● Add title and grid
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
temps = np.array([28, 30, 32, 31, 29])
S = pd.Series(temps)
print(S)
plt.plot(S)
plt.title('Daily Temperature')
plt.grid(True)
plt.show()