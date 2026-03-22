import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is already defined/loaded from your dataset
# 3. DATA EXPLORATION
# ========================================
print("\nMissing Values:")
print(df.isnull().sum()) # Changed display() to print() for standard .py scripts

plt.figure()
sns.histplot(df['charges'], kde=True)
plt.title("Distribution of Medical Charges")
plt.show()

plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()