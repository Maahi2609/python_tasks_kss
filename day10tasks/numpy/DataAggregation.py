'''A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total'''

import numpy as np
arr1 = np.array([[10, 20], [30, 40]])
arr2 = np.array([[5, 15], [25, 35]])
arr = np.concatenate((arr1, arr2))
print(arr)
arr = np.sum(arr)
print(arr)