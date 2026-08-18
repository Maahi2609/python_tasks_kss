'''Scenario:
A shop records monthly sales:
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
Task:
● Convert data into a Pandas DataFrame
● Plot a line graph
● Label X-axis as months and Y-axis as sales'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]
data = pd.DataFrame(sales)
print(data)
plt.plot(months, sales)
plt.title('Line Graph')
plt.ylabel('sales')
plt.xlabel('months')
plt.show()
