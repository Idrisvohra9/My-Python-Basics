import pandas as pd

# Creating a series 
cols = [10,20,30]

print(pd.Series(cols, index=["a","b","c"]))