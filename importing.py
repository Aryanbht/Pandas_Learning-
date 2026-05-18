import pandas as pd

df = pd.read_csv("sample_sales_data.csv" , index_col = "Transaction_ID")
# print(df.to_string())

# df = pd.read_json("json_data.json")
# print(df.to_string())

# Selection By Column Name
# print(df["Date"].to_string())

# print(df[["Date","Transaction_ID","Product_Category"]].to_string())

# print(df.to_string())

# print(df.loc["TXN-01001" : "TXN-01012", ["Date", "Product_Category"]].to_string())

print(df.iloc[2:10:2 , 0:3].to_string())

userInput = input("Enter Your Product:")

try:
    print(df[df["Product_Category"] == userInput].to_string())
except KeyError :
    print(f"Product '{userInput}' not found in the dataFrame.")




