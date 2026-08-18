'''A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row
'''
import numpy as np
data = np.arange(1, 13)
data = data.reshape(3, 4)
print(data)
print(np.mean(data, axis=1))