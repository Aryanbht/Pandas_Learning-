import pandas as pd

#Aggregation is the process of summarizing data by applying a function to groups of data. In pandas, we can use the groupby() method to perform aggregation on a DataFrame.

df = pd.read_csv("data.csv")
#! Whole DataFrame Aggregation
# print(df.mean(numeric_only=True)) 
# print(df.sum(numeric_only=True)) 
# print(df.min(numeric_only=True)) 
# print(df.max(numeric_only=True)) 
# print(df.count())
#! Single Column Aggregation

# print(df["Current_GPA"].mean()) 
# print(df["Current_GPA"].sum()) 
# print(df["Current_GPA"].min()) 
# print(df["Current_GPA"].max()) 
# print(df["Current_GPA"].count()) 

#! Grouped Aggregation

group = df.groupby("Gender")

print(group["Current_GPA"].mean()) 