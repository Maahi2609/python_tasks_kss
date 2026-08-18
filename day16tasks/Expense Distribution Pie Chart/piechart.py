'''Scenario:
Monthly expenses:
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
Task:
● Create a pie chart
● Show percentage distribution
'''

import matplotlib.pyplot as plt
import numpy as np
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]
explode = (0.1, 0, 0)
plt.pie(expenses, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expenses')
plt.show() 