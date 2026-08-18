'''Given marks of 5 students in 3 subjects:
marks = np.array([
[70, 80, 90],
[60, 75, 85],
[50, 65, 70],
[90, 95, 85],
[40, 55, 60]
])
Task:
● Calculate total marks of each student.
● Identify students whose total marks are above the class average.
'''

import numpy as np
arr = np.array([[70, 80, 90], [60, 75, 85], [50, 65, 70], [90, 95, 85], [40, 55, 60]])
arr = arr.sum(1)
avg = arr.mean()
print(arr)
print(arr[arr > avg])