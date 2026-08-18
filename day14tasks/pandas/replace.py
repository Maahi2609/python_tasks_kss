'''Two Series:
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
Task:
● Add both Series
● Explain why some values become NaN
● Replace NaN with 0 and compute final result'''

import pandas as pd 
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
S = S1 + S2
print("After adding:")
print(S)
final_S = S.fillna(0)
print("\nAfter replacing NaN with 0:")
print(final_S)

