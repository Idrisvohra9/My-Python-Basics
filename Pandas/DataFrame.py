import pandas as pd

# Making a table from dataset:
dataSet = {
    "brand": ["Mercedes","Ferrari","Porsche"],
    "model": [1991,1972,1955]
}

ds = pd.DataFrame(dataSet)
print(ds)