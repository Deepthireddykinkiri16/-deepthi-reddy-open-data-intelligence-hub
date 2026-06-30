import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Total passengers
print("\nTotal Passengers:", len(df))

# Survival count
print("\nSurvival Count:")
print(df["Survived"].value_counts())

# Gender count
print("\nGender Count:")
print(df["Sex"].value_counts())

# Passenger Class count
print("\nPassenger Class Distribution:")
print(df["Pclass"].value_counts())

# Average age
print("\nAverage Age:")
print(df["Age"].mean())

# Maximum Fare
print("\nMaximum Fare:")
print(df["Fare"].max())

# Minimum Fare
print("\nMinimum Fare:")
print(df["Fare"].min())