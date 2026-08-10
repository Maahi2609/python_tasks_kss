'''Temperatures recorded in a city:
temps = np.array([28, 32, 35, 31, 29, 40, 38])
Task:
● Identify days where temperature is greater than 30.
● Return their indices.'''

import numpy as np
temps = np.array([28, 32, 35, 31, 29, 40, 38])
temp = temps > 30
temp = np.where(temp)
print(temp)