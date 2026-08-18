'''A Series contains:
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])
Task:
● Access values for B and D
● Return them as a subset'''

import pandas as pd
S = pd.Series([100, 200, 300, 400], index = ["A", "B", "C", "D"])
S = S[["B", "D"]]
print(S)