import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
 
# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------
 
df = pd.read_csv("cardata.csv")
 
print("=" * 60)
print("CARS DATA ANALYSIS - SCENARIO 1")
print("=" * 60)
 
 
# ------------------------------------------------------------
# 3. DISPLAY FIRST 5 ROWS
# ------------------------------------------------------------
 
print("\nFIRST 5 ROWS:")
print(df.head())
 
 
# ------------------------------------------------------------
# 4. DISPLAY LAST 5 ROWS
# ------------------------------------------------------------
 
print("\nLAST 5 ROWS:")
print(df.tail())
 
 
# ------------------------------------------------------------
# 5. DISPLAY COLUMN NAMES
# ------------------------------------------------------------
 
print("\nCOLUMN NAMES:")
print(df.columns)
 
 
# ------------------------------------------------------------
# 6. DISPLAY SHAPE OF DATASET
# ------------------------------------------------------------
 
print("\nSHAPE OF DATASET:")
print(df.shape)
 
 
# ------------------------------------------------------------
# 7. CHECK DATA TYPES
# ------------------------------------------------------------
 
print("\nDATA TYPES:")
print(df.dtypes)
 
 
# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------
 
print("\nMISSING VALUES:")
print(df[
    [
        "Selling_Price",
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type"
    ]
].isnull().sum())
 
 
# ------------------------------------------------------------
# 9. CONVERT NUMERIC COLUMNS TO NUMERIC TYPE
# ------------------------------------------------------------
 
df["Selling_Price"] = pd.to_numeric(
    df["Selling_Price"],
    errors="coerce"
)
 
df["Present_Price"] = pd.to_numeric(
    df["Present_Price"],
    errors="coerce"
)
 
df["Kms_Driven"] = pd.to_numeric(
    df["Kms_Driven"],
    errors="coerce"
)
 
df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)
 
 
# ------------------------------------------------------------
# 10. HANDLE MISSING VALUES
# ------------------------------------------------------------
 
# Numeric columns → Mean
 
df["Selling_Price"] = df["Selling_Price"].fillna(
    df["Selling_Price"].mean()
)
 
df["Present_Price"] = df["Present_Price"].fillna(
    df["Present_Price"].mean()
)
 
df["Kms_Driven"] = df["Kms_Driven"].fillna(
    df["Kms_Driven"].mean()
)
 
 
# Categorical column → Mode
 
df["Fuel_Type"] = df["Fuel_Type"].fillna(
    df["Fuel_Type"].mode()[0]
)
 
 
# ------------------------------------------------------------
# 11. CONVERT SELLING PRICE TO NUMPY ARRAY
# ------------------------------------------------------------
 
selling_price_array = df["Selling_Price"].to_numpy()
 
 
# ------------------------------------------------------------
# 12. CONVERT KMS DRIVEN TO NUMPY ARRAY
# ------------------------------------------------------------
 
kms_driven_array = df["Kms_Driven"].to_numpy()
 
 
# ------------------------------------------------------------
# 13. NUMPY CALCULATIONS
# ------------------------------------------------------------
 
minimum_selling_price = np.min(selling_price_array)
 
maximum_selling_price = np.max(selling_price_array)
 
average_selling_price = np.mean(selling_price_array)
 
 
# ------------------------------------------------------------
# 14. DISPLAY RESULTS
# ------------------------------------------------------------
 
print("\n" + "=" * 60)
print("NUMPY CALCULATIONS")
print("=" * 60)
 
print("\nMinimum Selling Price:",
      minimum_selling_price)
 
print("Maximum Selling Price:",
      maximum_selling_price)
 
print("Average Selling Price:",
      average_selling_price)
 
 
# ------------------------------------------------------------
# 15. FINAL MISSING VALUE CHECK
# ------------------------------------------------------------
 
print("\nFINAL MISSING VALUE CHECK:")
print(
    df[
        [
            "Selling_Price",
            "Present_Price",
            "Kms_Driven",
            "Fuel_Type"
        ]
    ].isnull().sum()
)
 
 
# ------------------------------------------------------------
# 16. FINAL MESSAGE
# ------------------------------------------------------------
 
print("\n" + "=" * 60)
print("SCENARIO 1 COMPLETED SUCCESSFULLY")
print("=" * 60)
 
# ============================================================
#                 SCENARIO 2
#             Selling Price Trend
#                 Line Graph
# ============================================================
 
print("\n" + "=" * 60)
print("SCENARIO 2: SELLING PRICE TREND")
print("=" * 60)
 
 
# ------------------------------------------------------------
# 1. SELECT REQUIRED COLUMNS
# ------------------------------------------------------------
 
sample = df[["Car_Name", "Selling_Price"]]
 
 
# ------------------------------------------------------------
# 2. TAKE FIRST 10 ROWS
# ------------------------------------------------------------
 
sample = sample.head(10)
 
print("\nFIRST 10 CARS:")
print(sample)
 
 
# ------------------------------------------------------------
# 3. CONVERT SELLING PRICE INTO NUMPY ARRAY
# ------------------------------------------------------------
 
selling_price_array = sample["Selling_Price"].to_numpy()
 
print("\nSELLING PRICE NUMPY ARRAY:")
print(selling_price_array)
 
 
# ------------------------------------------------------------
# 4. CREATE X-AXIS VALUES
# ------------------------------------------------------------
 
x_values = np.arange(len(selling_price_array))
 
print("\nX-AXIS VALUES:")
print(x_values)
 
 
# ------------------------------------------------------------
# 5. CREATE LINE GRAPH
# ------------------------------------------------------------
 
plt.figure(figsize=(10, 5))
 
plt.plot(
    x_values,
    selling_price_array,
    marker="o"
)
 
 
# ------------------------------------------------------------
# 6. ADD TITLE AND LABELS
# ------------------------------------------------------------
 
plt.title("Selling Price Trend (First 10 Cars)")
 
plt.xlabel("Row Index")
 
plt.ylabel("Selling Price")
 
 
# ------------------------------------------------------------
# 7. ADD GRID
# ------------------------------------------------------------
 
plt.grid(True)
 
 
# ------------------------------------------------------------
# 8. SAVE GRAPH
# ------------------------------------------------------------
 
plt.savefig(
    "Graph/selling_price_line.png",
    bbox_inches="tight"
)
 
 
# ------------------------------------------------------------
# 9. DISPLAY GRAPH
# ------------------------------------------------------------
 
plt.show()
 
plt.close()
 
 
# ------------------------------------------------------------
# 10. SUCCESS MESSAGE
# ------------------------------------------------------------
 
print("\nScenario 2 graph saved successfully.")
 
print("=" * 60)
print("SCENARIO 2 COMPLETED SUCCESSFULLY")
print("=" * 60)


#Scenario 3: Expensive Cars Analysis (Filtering + Bar)

'''Tasks: 
● Filter cars where: 
○ Selling_Price > 10 
● Group the filtered data by: 
○ Fuel_Type 
● Count number of cars in each fuel type. 
● Convert: 
○ fuel type labels 
○ counts 
into NumPy arrays. 
● Plot a bar chart using Matplotlib: 
○ X-axis → Fuel Type 
○ Y-axis → Count of expensive cars 
● Add: 
○ title 
○ x-label 
○ y-label 
● Save the graph.'''


# Filter expensive cars
expensive_cars = df(df["Selling_Price"] > 10)

# Group by Fuel_Type and count cars
fuel_counts = expensive_cars["Fuel_Type"].value_counts()

# Convert labels and counts to NumPy arrays
fuel_types = np.array(fuel_counts.index)
counts = np.array(fuel_counts.values)

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(fuel_types, counts)

plt.title("Fuel Type Distribution Among Expensive Cars")
plt.xlabel("Fuel Type")
plt.ylabel("Count of Expensive Cars")

plt.tight_layout()
plt.savefig("Graph/expensive_cars_fuel_type.png")


#Scenario 4: Fuel Type Distribution (Pie Chart)
''''
Tasks: 
● Count the number of cars in each: 
○ Fuel_Type 
● Select all categories or top categories if needed. 
● Prepare: 
○ labels 
○ values 
● Convert values into a NumPy array. 
● Plot a pie chart using Matplotlib. 
● Add: 
○ percentage labels 
○ title 
● Save the graph.'''

import numpy as np
import matplotlib.pyplot as plt

# Count cars in each fuel type
fuel_counts = df["Fuel_Type"].value_counts()

# Prepare labels and values
labels = np.array(fuel_counts.index)
values = np.array(fuel_counts.values)

# Plot pie chart
plt.figure(figsize=(7, 7))
plt.pie(
    values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Overall Distribution of Cars by Fuel Type")

plt.tight_layout()
plt.savefig("Graph/fuel_type_distribution.png")

