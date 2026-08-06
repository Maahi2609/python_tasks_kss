'''An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1, 2],
[3, 4]]
Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices.
'''

import numpy as np
arr = np.array([[1, 2], [3, 4]])
print("transpose matrix : ")
print(arr.transpose())
print("original matrix : ")
print(arr)