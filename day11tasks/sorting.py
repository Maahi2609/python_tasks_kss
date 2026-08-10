'''A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.'''

import numpy as np
arr = np.array(["Ravi", "Anil", "Sita", "John"])
arr.sort()
print(arr)