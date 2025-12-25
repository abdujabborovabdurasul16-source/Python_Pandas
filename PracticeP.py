from typing import Any

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray, dtype, float64

# Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 28],
    "Score": [85, 90, 78, 88, 95]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
#print("Original DataFrame:")
#print(df)

# Basic statistics
#print("\nSummary statistics:")
#print(df.describe())

# Filter rows (Age > 30)
#print("\nPeople older than 30:")
#print(df[df["Age"] > 30])

# Sort by Score
#print("\nSorted by Score:")
#print(df.sort_values(by="Score", ascending=False))

# Add a new column
#df["Passed"] = df["Score"] >= 80
#print("\nDataFrame with 'Passed' column:")
#print(df)

#Summary = df.info()
#dict1 = {'student': ['David', 'Samuel', 'Terry', 'Evan'], 'Age': [27, 24, 22, 32], 'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks': [85, 72, 89, 76] }
#df = pd.DataFrame(dict1)
x = np.linspace(0, np.pi, 50)
y = np.sin(x)
plt.plot(x, y)
plt.show()
