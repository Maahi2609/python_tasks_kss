'''Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.'''

import numpy as np
arr = np.array([10, 20, 30, 40])
copy_arr = arr.copy()
arr[0] = 100
print("Original:", arr)
print("Copy:", copy_arr)
view_arr = arr.view()
arr[1] = 200
print("Original:", arr)
print("View:", view_arr)