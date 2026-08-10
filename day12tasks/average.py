'''Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.'''

import numpy as np
sales = np.random.randint(100, 501, 10)
print(sales)
average = np.mean(sales)
print("average sales : ",average)