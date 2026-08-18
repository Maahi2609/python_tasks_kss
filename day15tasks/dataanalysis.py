'''Scenario:
Analyze student marks.
Task:
● Generate marks using NumPy
● Convert into Pandas DataFrame
● Use conditions to filter passing students
● Calculate mean using math/NumPy
● Use loop to print result.'''

import pandas as pd
import numpy as np
import math
np.random.seed(10)
marks = np.random.randint(0, 101, 10)
students = ["Stu1", "Stu2", "Stu3", "Stu4", "Stu5",
            "Stu6", "Stu7", "Stu8", "Stu9", "Stu10"]

df = pd.DataFrame({"Student": students, "Marks": marks})
print("Student Marks:")
print(df)
passing_students = df[df["Marks"] >= 40]
print("\nPassing Students:")
print(passing_students)
mean_marks = np.mean(df["Marks"])

print("Mean Marks:", mean_marks)
print("Results:")
for index, row in df.iterrows():
    if row["Marks"] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(row["Student"], "-", row["Marks"], "-", result)