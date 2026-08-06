'''A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part'''

import numpy as np
arr = np.array([12, 7, 25, 3, 18, 10])
arr.sort()
print(arr)
arr = np.array_split(arr, 2)
print(arr)
print("sum of first part : ",arr[0].sum())
print("sum of second part : ",arr[1].sum())