'''Scenario:
scores = np.array([40, 60, 80, 30, 90])
Task:
● Categorize into:
○ Pass (>50)
○ Fail (<=50)
● Count using NumPy/Pandas
● Plot pie chart for Pass vs Fail.'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
scores = np.array([40, 60, 80, 30, 90])
S = pd.Series(scores)
S = S[scores > 50]
print("Pass")
print(S)
pass_count = len(S)
S = pd.Series(scores)
S = S[scores <= 50]
print("Fail")
print(S)
fail_count = len(S)
labels = ("Pass", "Fail")
count = (pass_count, fail_count)
plt.pie(count, labels=labels, autopct='' \
'%1.1f%%', startangle=90)
plt.title('Pass vs Fail')
plt.show()
