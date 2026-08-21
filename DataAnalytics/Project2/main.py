import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

#Scenario 1: Data Loading & Preprocessing
#1. Load the dataset using Pandas.
df = pd.read_csv("ign.csv")

#Display First 5 rows
print("First 5 rows.")
print(df.head())

# Display Last 5 rows
print("\nLast 5 rows.")
print(df.tail())

# Display shape
print("\nShape of dataset:")
print(df.shape)

# 3. Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"])

# 4. Check for missing values
print("\nMissing values:")
print(df[["score", "genre", "platform"]].isnull().sum())

# 5. Handle missing values

# Fill score with mean
df["score"] = df["score"].fillna(df["score"].mean())

# Fill genre with mode
df["genre"] = df["genre"].fillna(df["genre"].mode()[0])

# 6. Ensure correct data types

# score -> float
df["score"] = df["score"].astype(float)

# release_year, release_month, release_day -> integer
df["release_year"] = df["release_year"].astype(int)
df["release_month"] = df["release_month"].astype(int)
df["release_day"] = df["release_day"].astype(int)

# Check final data types
print("\nFinal data types:")
print(df.dtypes)

# Check missing values after handling
print("\nMissing values after handling:")
print(df[["score", "genre", "platform"]].isnull().sum())

#Scenario 2: Line Graph (Score Trend) + Save

# Group by release_year and calculate average score
avg_score_by_year = df.groupby("release_year")["score"].mean()

# Convert results to NumPy arrays
years = avg_score_by_year.index.to_numpy()
average_scores = avg_score_by_year.to_numpy()

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(years, average_scores, marker="o")

# Add title and axis labels
plt.title("Average Game Score Over Years")
plt.xlabel("release_year")
plt.ylabel("average score")

# Improve readability
plt.grid(True)
plt.tight_layout()

# Save the graph
plt.savefig("avg_score_trend.png")

# Display the graph
plt.show()

#Scenario 3: Filtering + Bar Chart + Save

#1. Filter dataset where:
high_rated = df[df["score"] > 7]

# 2. Count high-rated games per platform
platform_counts = high_rated["platform"].value_counts()

# 3. Select top 10 platforms
top_10_platforms = platform_counts.head(10)

# 4. Convert data into NumPy arrays
platforms = top_10_platforms.index.to_numpy()
counts = top_10_platforms.to_numpy()

# 5. Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(platforms, counts)

# 6. Rotate x-axis labels
plt.xticks(rotation=45)

plt.xlabel("Platform")
plt.ylabel("Count of Games")
plt.title("Top 10 Platforms with High-Rated Games")

plt.tight_layout()

# Save the graph
plt.savefig("top_platforms_bar.png")

# Display the graph
plt.show()

#Scenario 4: Aggregation + Pie Chart + Save

# 1. Count the number of games per genre
count_genre = df["genre"].value_counts()

# 2. Select the top 5 genres
top_5_genres = count_genre.head(5)

# 3. Prepare labels and values
labels = top_5_genres.index
values = top_5_genres.values

# 4. Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels = labels, autopct = '%1.1f%%', startangle = 90)
plt.title("Top 5 Game Genres Distribution")

# 5. Save the graph
plt.savefig("genre_distribution.png", bbox_inches="tight")
plt.show()

#Scenario 5: Advanced Analysis + Multiple Graphs

# 1. Create score_category
# 1. Create score_category
df["score_category"] = np.select(
    [
        df["score"] >= 9,
        (df["score"] >= 7) & (df["score"] < 9),
        df["score"] < 7
    ],
    [
        "Excellent",
        "Good",
        "Average"
    ],
    default="Average"
)


# 2. Convert editors_choice: Y → 1, N → 0
df["editors_choice"] = df["editors_choice"].map({"Y": 1, "N": 0})

#Part-2 NumPy Analysis

#3. Use NumPy to: 
# Calculate yearly score growth 
yearly_scores = df.groupby("release_year")["score"].mean().sort_index()

# using np.diff() on average yearly scores
yearly_growth = np.diff(yearly_scores.values)

print("Yearly score growth:")
print(yearly_growth)

#np.diff() calculates:
#Current year's average score - Previous year's average score

#Part-3: Visualizations
#Line Graph
#4. Plot trend of: 
#     -Average score per release_year 
plt.figure(figsize=(10, 6))
plt.plot(yearly_scores.index, yearly_scores.values, marker="o")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.title("Average Score per Release Year")
plt.grid(True)
plt.savefig("score_trend.png", bbox_inches="tight")
plt.show()

#Stacked Bar Chart 
#5. Show count of: 
#     -score_category per release_year 
category_counts = pd.crosstab(
    df["release_year"],
    df["score_category"]
)

category_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.title("Score Category Distribution per Release Year")
plt.legend(title="Score Category")

plt.savefig("score_category_stacked.png", bbox_inches="tight")
plt.show()

#Histogram 
# 6.Plot distribution of: 
#         -Score
plt.figure(figsize=(8, 6))

plt.hist(df["score"].dropna(), bins=20, edgecolor="black")

plt.xlabel("Score")
plt.ylabel("Number of Games")
plt.title("Score Distribution")

plt.savefig("score_distribution.png", bbox_inches="tight")
plt.show()

#Part 5: Insights
# Years with the highest average scores
highest_score = yearly_scores.max()
highest_years = yearly_scores[yearly_scores == highest_score]

print("Highest scoring year(s):")
print(highest_years)

# Check whether scores increased over time
growth = yearly_scores.iloc[-1] - yearly_scores.iloc[0]

if growth > 0:
    print("Average scores increased over time.")
elif growth < 0:
    print("Average scores decreased over time.")
else:
    print("Average scores remained approximately the same.")

# Editors' Choice and high scores
editor_comparison = df.groupby("editors_choice")["score"].mean()

print("\nAverage score by Editors' Choice:")
print(editor_comparison)
 



