Data structures at a glance

| name      | description                                                                                       |
|:----------|:--------------------------------------------------------------------------------------------------|
| Series    | 1D labeled homogeneously-typed array                                                              |
| DataFrame | General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns |
| Panel     | General 3D labeled, also size-mutable array                                                       |


import pandas as pd import numpy as np import matplotlib.pyplot as plt

1 Object Creation
-----------------

+ s = pd.Series([1,3,5,np.nan,6,8])
+ dates = pd.date_range('20130101', periods=6)
+ df = pd.DataFrame(np.random.randn(6,4), index=dates,
  columns=list('ABCD'))
+ df2.dtypes,df2.<TAB>

2 Viewing Data
--------------

+ df.head()
+ df.tail(3)
+ df.index
+ df.columns
+ df.values
+ df.describe()
+ df.T
+ df.sort_index(axis=1, ascending=False)
+ df.sort_values(by='B')

3 Selection(.at, .iat, .loc, .iloc and .ix.)
--------------------------------------------

+ Getting:Selecting a single column
    - df['A']
    - df[0:3]
+ Selection by Label
    - df.loc[dates[0]]
    - df.loc[:,['A','B']]
    - df.loc['20130102':'20130104',['A','B']]
+ Selection by Position
    - df.iloc[3]
    - df.iat[1,1]
+ Boolean Indexing
    - df[df.A > 0]
    - df[df > 0]
    - df2[df2['E'].isin(['two','four'])]
+ Setting
    - Setting a new column automatically aligns the data by the
      indexes:df['F'] = s1
    - Setting values by label:df.at[dates[0],'A'] = 0
    - Setting values by position:df.iat[0,1] = 0
    - Setting by assigning with a numpy array:df.loc[:,'D'] =
      np.array([5] * len(df))
    - A where operation with setting.

4 Missing Data
--------------

+ Reindexing:df1 = df.reindex(index=dates[0:4], columns=list(df.columns)
+ ['E'])
+ drop any rows that have missing data:df1.dropna(how='any')
+ Filling missing data:df1.fillna(value=5)

5 Operations
------------

+ Stats:Operations in general exclude missing data.
    - Performing a descriptive statistic:df.mean()
    - Same operation on the other axis:df.mean(1)
    - pandas automatically broadcasts along the specified dimension:s =
      pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
    - df.sub(s, axis='index')
+ Apply:Applying functions to the data
    - df.apply(np.cumsum)
    - df.apply(lambda x: x.max() - x.min())
+ Histogramming:直方图
    - s.value_counts()
+ String Methods
    - s.str.lower()

6 Merge
-------

+ Concat:ombining together Series, DataFrame, and Panel objects with
  various kinds of set logic for the indexes and relational algebra
  functionality in the case of join / merge-type operations.
    - pieces = [df[:3], df[3:7], df[7:]], pd.concat(pieces)
+ Join:SQL style merges.
    - left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    - right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    - pd.merge(left, right, on='key')
+ Append:Append rows to a dataframe
    - s = df.iloc[3]
    - df.append(s, ignore_index=True)

7 Grouping
----------

+ Splitting the data into groups based on some criteria:
+ Applying a function to each group independently:
  df.groupby('A').sum(),df.groupby(['A','B']).sum()
+ Combining the results into a data structure

8 Reshaping
-----------

+ Stack:method “compresses” a level in the DataFrame’s columns. stacked
  = df2.stack(), stacked.unstack(0)
+ Pivot Tables(数据透视表):pd.pivot_table(df, values='D',
  index=['A', 'B'], columns=['C'])

9 Time Series
-------------

+ resample, date_range:rng = pd.date_range('1/1/2012', periods=100,
  freq='S'), ts = pd.Series(np.random.randint(0, 500, len(rng)),
  index=rng), ts.resample('5Min').sum()
+ Time zone representation: ts.tz_localize('UTC')
+ Convert to another time zone: ts_utc.tz_convert('US/Eastern')
+ Converting between time span representations: ps = ts.to_period(),
  ps.to_timestamp()
+ convert a quarterly frequency:prng = pd.period_range('1990Q1',
  '2000Q4', freq='Q-NOV'), ts = pd.Series(np.random.randn(len(prng)),
  prng), ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9,
  ts.head()

10 Categoricals
---------------
+ Convert the raw grades to a categorical data type:
    - df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
    - df["grade"] = df["raw_grade"].astype("category")
+ Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!)
    - df["grade"].cat.categories = ["very good", "good", "very bad"]
+ Reorder the categories and simultaneously add the missing categories (methods under Series .cat return a new Series per default).
    - df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
+ Sorting is per order in the categories, not lexical order.
    - df.sort_values(by="grade")
+ Grouping by a categorical column shows also empty categories.
    - df.groupby("grade").size()

11 Plotting
-----------
- ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
- ts = ts.cumsum()
- plt.figure(); df.plot(); plt.legend(loc='best')

12 Getting Data In/Out
----------------------
+ CSV
    - df.to_csv('foo.csv')
    - pd.read_csv('foo.csv')
+ HDF5
    - df.to_hdf('foo.h5','df')
    - pd.read_hdf('foo.h5','df')
+ Excel
    - df.to_excel('foo.xlsx', sheet_name='Sheet1')
    - pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
+ Gotchas

















