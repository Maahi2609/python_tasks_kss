'''Scenario:
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → daily temperature trend
○ Bar chart → day-wise temperature
○ Pie chart → proportion of high (>30) vs low temps
○ Histogram → temperature frequency
○ Scatter plot → day index vs temperature
.'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
data = pd.DataFrame({"temps":temps, "days":days})

plt.plot(data["days"], data["temps"])
plt.title('Daily Temperature Trend')
plt.xlabel('Days')
plt.ylabel('Temps')
plt.show()

plt.bar(data["days"], data["temps"])
plt.title('Day-Wise Temperature')
plt.xlabel('Days')
plt.ylabel('High Temps')
plt.show()

high_data = data[temps > 30]
print("High")
print(high_data)
low_data = data[temps < 30]
print("Low")
print(low_data)

high_count = len(high_data)
low_count = len(low_data)

plt.pie([high_count, low_count], labels = ["High", "Low"], autopct = '%1.1f%%', startangle = 90)
plt.title('Proportion of High (>30) vs Low Temps')
plt.xlabel('high_data')
plt.ylabel('days')
plt.show()

plt.hist(days, bins=4, histtype="bar")
plt.title('temperature frequency')
plt.xlabel('temperature')
plt.ylabel('frequency')
plt.show()

day_index = np.arange(1, 8)
plt.scatter(day_index, temps)
plt.title(' Day Index vs Temperature')
plt.xlabel('day_index')
plt.ylabel('temps')
plt.show()