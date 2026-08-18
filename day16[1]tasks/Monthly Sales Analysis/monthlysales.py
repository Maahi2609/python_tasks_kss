'''Scenario:
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → month-wise comparison
○ Pie chart → contribution of each month
○ Histogram → frequency of sales values
○ Scatter plot → month index vs sales
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
data = pd.DataFrame({"sales":sales, "months":months})
print(data)
plt.plot(data['months'], data['sales'])
plt.title('sales trend')
plt.xlabel('months')
plt.ylabel('sales')
plt.show()


plt.bar(data['months'], data['sales'])
plt.title('Month-Wise Comparison')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()


plt.pie(sales, labels = months, autopct='%1.1f%%', startangle = 90)
plt.title('Contribution of Each Month')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()


plt.hist(sales, bins = 3, histtype='bar')
plt.title('Frequency of Sales Values')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

month_index = np.arange(1, 7)
plt.scatter(month_index, sales)
plt.title('Month Index vs Sales')
plt.xlabel('Month_Index')
plt.ylabel('Sales')
plt.show()