'''Scenario:
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
Task:
● Create DataFrame
● Plot:
○ Line graph → sales trend
○ Bar chart → product vs sales
○ Pie chart → sales contribution
○ Histogram → profit distribution
○ Scatter plot → sales vs profit.'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]
data = pd.DataFrame({"sales":sales, "profit":profit, "products":products})
print(data)

plt.plot(data['products'], data['sales'], marker = 'o')
plt.title('Sales Trend')
plt.xlabel('profit, products')
plt.ylabel('sales')
plt.show()

plt.bar(data['products'], data['sales'])
plt.title('product vs sales')
plt.xlabel('products')
plt.ylabel('sales')
plt.show()

plt.pie(sales, labels = products, autopct='%1.1f%%', startangle=90 )
plt.title('Sales Contribution')
plt.xlabel('products')
plt.ylabel('sales')
plt.show()

plt.hist(profit, bins=4, histtype="bar")
plt.title('Profit Distribution')
plt.xlabel('profit')
plt.ylabel('frequency')
plt.show()

plt.scatter(sales, profit)
plt.title('sales vs profit')
plt.xlabel('sales')
plt.ylabel('profit')
plt.show()