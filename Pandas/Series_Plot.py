import pandas as pd
# Corona Cases of Gujarat in 2021
data = [16000,8000,120,10,30,40,580,1100,300,100,30,12]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

s = pd.Series(data, index=months)

s.plot(kind='line',title="Corona Cases of Gujarat in 2021",xlabel="months",ylabel="data")
