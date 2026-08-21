import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ============================================================
# Scenario 1: Basic Data Loading & Cleaning
# ============================================================

# 1. Load CSV file
df = pd.read_csv("railway_gauges.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# 2. Display first 5 rows and column names
print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

# 3. Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Replace missing values with 0
df = df.fillna(0)

df["Year_Number"] = df["Year"].str[:4].astype(int)
# 4. Convert gauge columns to numeric
df["Broad Gauge"] = pd.to_numeric(df["Broad Gauge"])
df["Metre Gauge"] = pd.to_numeric(df["Metre Gauge"])
df["Narrow Gauge"] = pd.to_numeric(df["Narrow Gauge"])
df["Total"] = pd.to_numeric(df["Total"])

print("\nData types:")
print(df.dtypes)

# ============================================================
# Scenario 2: Simple Visualization
# ============================================================

# Extract Year and Total columns
year_total = df[["Year", "Total"]]

print("\nYear and Total:")
print(year_total)

# Plot a line graph
plt.plot(year_total["Year"], year_total["Total"])

plt.title("Total Railway Tracks Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")
plt.grid(True)
plt.savefig("Graph/Total_railway_growth.png")
plt.close()


# Identify trend
first_total = year_total["Total"].iloc[0]
last_total = year_total["Total"].iloc[-1]

if last_total > first_total:
    print("Trend is increasing.")
elif last_total < first_total:
    print("Trend is decreasing.")
else:
    print("Trend remains the same.")


# ============================================================
# Scenario 3: Filtering + Bar Chart
# ============================================================

# Filter the dataset for years after 2000
df["Year"] = df["Year"].str[:4].astype(int)
recent_df = df[df["Year"] > 2000]

# Select the three gauge columns
gauge_data = recent_df[
    ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge"]
]

print("\nGauge data after 2000:")
print(gauge_data)

# Plot grouped bar chart
gauge_data.plot(
    x="Year",
    kind="bar",
    figsize=(10, 6)
)

plt.title("Railway Gauges After 2000")
plt.xlabel("Year")
plt.ylabel("Number of Railway Tracks")

plt.legend([
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"
])

plt.xticks(rotation=70)
plt.tight_layout()

plt.savefig("Graph/fig.png")
plt.close()


# Identify dominant gauge
totals = recent_df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

dominant_gauge = totals.idxmax()

print("\nDominant gauge after 2000:", dominant_gauge)


# ============================================================
# Scenario 4: Feature Engineering + Pie Chart
# ============================================================

# Calculate total sum of each gauge
total_gauges = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("\nTotal of each gauge:")
print(total_gauges)

# Plot pie chart
total_gauges.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7, 7)
)

plt.title("Percentage Contribution of Railway Gauges")
plt.ylabel("")

plt.savefig("Graph/fig2.png")
plt.close()


# Identify gauge with highest contribution
dominant_gauge = total_gauges.idxmax()

print("\nGauge contributing the most:", dominant_gauge)


# ============================================================
# Scenario 5: Advanced Analysis
# ============================================================

# Create percentage columns
df["Broad Gauge %"] = (
    df["Broad Gauge"] / df["Total"]
) * 100

df["Metre Gauge %"] = (
    df["Metre Gauge"] / df["Total"]
) * 100

df["Narrow Gauge %"] = (
    df["Narrow Gauge"] / df["Total"]
) * 100


# Display the new columns
print("\nPercentage contribution:")

print(
    df[
        [
            "Year",
            "Broad Gauge %",
            "Metre Gauge %",
            "Narrow Gauge %"
        ]
    ]
)


# Calculate yearly growth of Total tracks using np.diff()
growth = np.diff(df["Total"])


# Add growth to the DataFrame
df["Total Growth"] = np.nan

df.loc[1:, "Total Growth"] = growth


print("\nYearly growth of Total tracks:")

print(
    df[
        ["Year", "Total", "Total Growth"]
    ]
)


# ============================================================
# Line graph for all gauges
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Broad Gauge"],
    label="Broad Gauge"
)

plt.plot(
    df["Year"],
    df["Metre Gauge"],
    label="Metre Gauge"
)

plt.plot(
    df["Year"],
    df["Narrow Gauge"],
    label="Narrow Gauge"
)

plt.title("Railway Gauges Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")
plt.legend()
plt.grid(True)

plt.savefig("Graph/fig3_line.png")
plt.close()


# ============================================================
# Stacked bar chart
# ============================================================

df.plot(
    x="Year",
    y=[
        "Broad Gauge",
        "Metre Gauge",
        "Narrow Gauge"
    ],
    kind="bar",
    stacked=True,
    figsize=(10, 6)
)

plt.title("Composition of Railway Gauges Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Tracks")

plt.legend()

plt.xticks(rotation=70)
plt.tight_layout()

plt.savefig("Graph/fig4_stacked.png")
plt.close()


# ============================================================
# Find the year with the highest growth
# ============================================================

highest_growth_index = (
    df["Total Growth"].idxmax()
)

print("\nYear with highest growth:")

print(
    df.loc[
        highest_growth_index,
        ["Year", "Total Growth"]
    ]
)


# ============================================================
# Check for decline in each gauge
# ============================================================

print("\nGauge declines:")

for gauge in [
    "Broad Gauge",
    "Metre Gauge",
    "Narrow Gauge"
]:

    decline = df[gauge].diff() < 0

    if decline.any():

        print(
            gauge,
            "shows a decline."
        )

        print(
            df.loc[
                decline,
                ["Year", gauge]
            ]
        )

    else:

        print(
            gauge,
            "has no decline."
        )


# ============================================================
# Find the dominant gauge
# ============================================================

gauge_totals = df[
    [
        "Broad Gauge",
        "Metre Gauge",
        "Narrow Gauge"
    ]
].sum()

dominant_gauge = gauge_totals.idxmax()

print("\nDominant gauge:", dominant_gauge)


# ============================================================
# Final Conclusion
# ============================================================

print("\nConclusion:")

print(
    "The gauge with the highest overall contribution is",
    dominant_gauge
)

print(
    "Check the percentage columns and graphs to determine "
    "whether the railway system is shifting towards a "
    "single dominant gauge."
)