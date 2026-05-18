import pandas as pd
df = pd.read_csv('data.csv')
print(df)

toppers = df[df["Current_GPA"] > 3.5]
male_students = df[df["Gender"] == "Male"]
male_toppers = df[(df["Current_GPA"] > 3.5) & (df["Gender"] == "Male")]
print(male_toppers)