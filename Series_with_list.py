import pandas as pd
import numpy as np

# A series I s a Pandas 1D labelled Array that can hold any Data Type.
# Think of like any single column in a spreadsheet.

list = [100, 200, 300, 400, 500]

# data = pd.Series(list , index = np.arange(1,6))
data = pd.Series(list , index = ["a", "b", "c", "d", "e"])
print(data)


print(data.loc["c"])
print(data.iloc[4])

print(data[data >= 200])
