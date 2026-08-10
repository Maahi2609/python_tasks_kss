'''Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered values'''


import numpy as np
values = np.random.rand(8)
print("Original values:", values)
values = values * 100
print("Values after multiplying by 100:", values)
filtered_values = values[values > 50]
sorted_values = np.sort(filtered_values)
print("Filtered values:", filtered_values)
print("Sorted values:", sorted_values)