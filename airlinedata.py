import pandas as pd 

df = pd.read_csv("Dataset/Airline Delay.csv")
print(df.head())
print(df.tail())

# Column Names
print(df.columns)

# Dataset Information
print(df.info())

# Missing Values
print(df.isnull().sum())

# Duplicate Rows
print(df.duplicated().sum())

# Remove Duplicate Rows
df = df.drop_duplicates()

# Check Missing Values
print(df.isnull().sum())

# Remove Rows with Missing Values
df = df.dropna()

df.to_csv("airline_data_cleaned.csv", index=False)
print("Cleaned Dataset Saved Successfully!")