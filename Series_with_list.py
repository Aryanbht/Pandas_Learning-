import pandas as pd

# A series I s a Pandas 1D labelled Array that can hold any Data Type.
# Think of like any single column in a spreadsheet.

list = [100 , 101 , 97 , 102 , 90 , 98]
series = pd.Series(list , index= ["a" , "b" , "c" , "d" , "e" , "f"])
print(series)
print(series.loc["a"]) ## Position By Label 

series.loc["b"] = 198

print(series)

print(series.iloc[0]) ## Position By Index 

print(series[series > 99 ])


