import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display first 5 rows
print(df.head())

# Dataset shape
print("\nShape:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn distribution
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Save output
df.to_csv("output.csv", index=False)

# Plot churn distribution
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()