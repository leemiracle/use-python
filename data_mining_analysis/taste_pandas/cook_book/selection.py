import pandas as pd
import numpy as np

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
# 1.DataFrames
df[(df.AAA <= 6) & (df.index.isin([0,2,4]))]

data = {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}
df = pd.DataFrame(data=data,index=['foo','bar','boo','kar'])

df.loc['bar':'kar'] #Label
df.ix[0:3] #Same as .iloc[0:3]
df[~((df.AAA <= 6) & (df.index.isin([0,2,4])))]

# 2.Panels
pf = pd.Panel({'df1':df1,'df2':df2,'df3':df3})

# 3 New Columns
# using applymap
source_cols = df.columns # or some subset would work too.
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1 : 'Alpha', 2 : 'Beta', 3 : 'Charlie' }
df[new_cols] = df[source_cols].applymap(categories.get)

# using min() with groupby
df.loc[df.groupby("AAA")["BBB"].idxmin()]
df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
