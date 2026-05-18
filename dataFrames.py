#A dataFrames is a collection of data organized in a tabular format, similar to a spreadsheet or a SQL table. It is a powerful data structure used in data analysis and manipulation, particularly in programming languages like Python (with libraries such as pandas) and R. A dataFrame allows you to store and manipulate heterogeneous data, meaning that different columns can contain different types of data (e.g., integers, floats, strings).


import pandas as pd

data = {
    "Name" : ["Aryan", "Rohan", "Sita"],
    "Age" : [25, 30 , 39]
}

df = pd.DataFrame(data , index = ["employee1", "employee2", "employee3"])
# print(df)

# print(df.loc["employee1"])
# print(df.iloc[0])

#Add a new column to the dataFrame

df["Job"] = ["Data Scientist", "Software Engineer", "Product Manager"]
print(df)

new_row = pd.DataFrame([{"Name": "Gita", "Age": 28, "Job": "Data Analyst"} ] , index = ["employee4"])
df = pd.concat([df, new_row])
print(df)