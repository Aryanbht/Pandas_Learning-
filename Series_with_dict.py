import pandas as pd
 
calories = {
    "Day-1" : 1780 ,
    "Day-2" : 2342 , 
    "Day-3" : 1879 ,
}

series = pd.Series(calories)
print(series)
print(series.loc["Day-1"])

series.loc["Day-3"] = 1923
series.loc["Day-1"] += 200

print(series)

print(series.iloc[0])

print(series[series >= 2000])
