'''Scenario:
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
Task:
● Create DataFrame
● Plot two line graphs on same plot
● Add legend
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = {
"Month": ["Jan", "Feb", "Mar"],
"Store_A": [100, 150, 200],
"Store_B": [90, 140, 210]
}
S = pd.DataFrame(data)
print(S)
plt.figure()
plt.plot(S["Month"], S["Store_A"], label = "Store A", linewidth = 5)
plt.plot(S["Month"], S["Store_B"], label = "Store B", linewidth = 5)
plt.title('Store Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()
