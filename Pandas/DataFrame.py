import pandas as pd

# Making a table from dataset:
dataSet = {
    "brand": ["Mercedes","Ferrari","Porsche"],
    "model": [1991,1972,1955]
}

# we can also provide index (an array of values) and access it with .loc[]
ds = pd.DataFrame(dataSet)

print(ds.loc[1])