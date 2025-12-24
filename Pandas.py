import pandas as pd

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 28],
    "Score": [85, 90, 78, 88, 95]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Filter rows (Age > 30)
print("\nPeople older than 30:")
print(df[df["Age"] > 30])

# Sort by Score
print("\nSorted by Score:")
print(df.sort_values(by="Score", ascending=False))

# Add a new column
df["Passed"] = df["Score"] >= 80
print("\nDataFrame with 'Passed' column:")
print(df)


