import pandas as pd

df = pd.read_csv("data.csv")

#Data Cleaning = the process of identifying and correcting (or removing) errors and inconsistencies in data to improve its quality and reliability. This can involve handling missing values, correcting data types, removing duplicates, and standardizing formats.

#Drop Irrelevant Columns

df1 = df.drop(columns=["Grade_Level"])
# print(df1)

# HAndle Missing Values

# df = df.dropna(subset=["Gender","Grade_Level"])
df = df.fillna({
    "Gender": "Unknown",
    "Grade_Level": "Unknown"
})
# print(df)

# Fix inconsistent data

df["Grade_Level"] = df["Grade_Level"].replace("10th", 10)

# print(df)

# Remove duplicates
df = df.drop_duplicates()
print(df)
