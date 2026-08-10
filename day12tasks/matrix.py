'''Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values.'''

import numpy as np
matrix = np.random.randint(0 , 51,(3, 3))
print("Matrix : ")
print(matrix)
filter_values = matrix[matrix > 25]
print("values greater than 25 : ")
print("flitered values : ",filter_values)