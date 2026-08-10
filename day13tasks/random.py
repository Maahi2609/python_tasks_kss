'''Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result'''

import numpy as np
nums = np.random.randint(1, 100, 10)
filtered = nums[nums % 5 == 0]
print(np.sort(filtered))
