import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,1), index=pd.date_range('2013-08-01', periods=6, freq='B'))
# np.nan:无数据
df.ix[3,'A'] = np.nan
# 填充
df.reindex(df.index[::-1]).ffill()
# Replace

