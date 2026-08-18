'''Scenario:
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
Task:
● Create DataFrame
● Plot bar chart
● Add labels and title.'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])
data = pd.DataFrame({"Product":products, "Sales":sales})
print(data)
plt.bar(data["Product"], data["Sales"])
plt.title('Stationary')
plt.xlabel('products')
plt.ylabel('sales')
plt.show()