import pandas as pd

# Load the dataset
df = pd.read_csv("shaft_dataset.csv")

# Display the first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Display information about the dataset
print("\nDATASET INFORMATION")
print(df.info())

# Display basic statistics
print("\nSTATISTICS")
print(df.describe())

# Count PASS and FAIL
print("\nPASS / FAIL COUNT")
print(df["status"].value_counts())