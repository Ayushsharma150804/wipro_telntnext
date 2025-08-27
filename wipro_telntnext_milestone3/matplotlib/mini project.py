
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Diabetes.csv")
print("✅ Data Loaded Successfully!\n")
print("Shape of dataset:", df.shape)
print(df.head())

print("\n📌 Data Info:")
print(df.info())

print("\n📌 Missing Values:")
print(df.isnull().sum())

print("\n📌 Statistical Summary:")
print(df.describe())

# Assuming 'Outcome' is categorical (0 = No Diabetes, 1 = Diabetes)
if 'Outcome' in df.columns:
    df['Outcome'] = df['Outcome'].astype('category')

print("\nUnique values per column:")
print(df.nunique())

print("\n📊 Univariate Analysis...")

df.hist(figsize=(12,10))
plt.suptitle("Histograms of Features")
plt.show()

for col in df.columns:
    plt.figure(figsize=(5,3))
    sns.boxplot(x=df[col], color="skyblue")
    plt.title(f"Boxplot of {col}")
    plt.show()

print("\n📊 Bivariate Analysis...")

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

if 'Outcome' in df.columns:
    sns.pairplot(df, hue="Outcome", diag_kind="kde")
    plt.suptitle("Pairplot of Features vs Outcome", y=1.02)
    plt.show()

if 'Outcome' in df.columns:
    for col in df.columns:
        if col != "Outcome":
            plt.figure(figsize=(5,3))
            sns.boxplot(x="Outcome", y=col, data=df, palette="Set2")
            plt.title(f"{col} vs Outcome")
            plt.show()
