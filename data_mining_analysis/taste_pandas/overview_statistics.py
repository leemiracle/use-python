import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.Series([1, 3, 5,np.nan,6,8])
# 空值数量
count_null_number = int(df.isnull().sum())
# 有数据条数
count_not_null_number = int(df.notnull().sum())
# 统计非数值 数量
not_numeric = int(pd.to_numeric(df, errors='coerce').isnull().sum())
# 值的集合
unique = int(df.nunique())
# 前5条数据
head_data = [str(i) for i in df.head(5).values]
# 后5条数据
tail_data = [str(i) for i in df.tail(5).values]


