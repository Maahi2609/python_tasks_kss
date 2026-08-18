'''Scenario:
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
Task:
● Create DataFrame
● Plot:
○ Line graph (trend)
○ Bar chart (comparison)
○ Pie chart (distribution)
● Show all in single figure (subplots).'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]
data = pd.DataFrame({"sales":sales,"products":products})
print(data)
plt.subplot(131)
plt.plot(data['sales'],data['products'])
plt.subplot(132)
plt.bar(data['sales'],data['products'])
plt.subplot(133)
plt.pie(sales, labels=products, autopct='%1.1f%%', startangle=90)
plt.suptitle('Categorical Plotting')
plt.show()