import pandas as pd
df = pd.DataFrame({'row':[0, 1, 2], 'One_X': [1.1, 1.1, 1.1]})
# 设置索引
df = df.set_index('row')
# 设置多重索引
df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])
# stock & reset
df = df.stock(0).reset_index(1)

