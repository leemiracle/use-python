import functools

import pandas as pd
import numpy as np
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})

# if-then
df.ix[df.AAA >= 5, ['BBB', 'CCC']] = -1 # if df.AAA >= 5 then df.BBB, df.CCC=-1, -1
# True/False DataFrame
df_mask = pd.DataFrame({'AAA': [True] * 4, 'BBB': [False] * 4, 'CCC': [True, False] * 2})
# False:填充-1000
df.where(df_mask, -1000)
# it>5:high, it<=5:low
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')


# Splitting
dflow = df[df.AAA <= 5]
dfhigh = df[df.AAA > 5]


# Building Criteria
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']

Crit1 = df.AAA <= 5.5
Crit2 = df.BBB == 10.0
Crit3 = df.CCC > -40.0
AllCrit = Crit1 & Crit2 & Crit3
CritList = [Crit1, Crit2, Crit3]
AllCrit = functools.reduce(lambda x,y: x & y, CritList)
df[AllCrit]

