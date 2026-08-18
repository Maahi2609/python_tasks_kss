'''A shop tracks fruit sales:
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
Task:
● Add both series
● Find the total sales of all fruits combined'''

import pandas as pd
S1 = pd.Series([10, 20, 30], index = ["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index = ["apple", "banana", "cherry"])
print(S1 + S2)
print("sum of S1 : ",sum(S1))
print("sum of S2 : ",sum(S2))
print("sum of S1 and S2 : ",sum(S1 + S2))