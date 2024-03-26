# -*- coding: utf-8 -*-
import pandas as pd, numpy as np
#%% Pandas: Series
"""
One-dimensional array-like object containing a sequence of values (can be any types)
    and an associated array of data labels, called its index.
Construction:
    pd.Series(data=None, 
              index=None, 
              dtype=None, 
              name=None, 
              copy=False, 
              fastpath=False)
    
        data: array-like, Iterable, dict, or scalar value
            Contains data stored in Series. 
            If data is a dict: key will become index, and value will become value.

        index: array-like or Index (1d)
            Values must have the same length as data. 
            Non-unique index values are allowed. 
            Will default to RangeIndex (0, 1, 2, …, n) if not provided. 
            If the index is not None, the resulting Series is reindexed with the index values.

        dtype: str, numpy.dtype, or ExtensionDtype, optional
            Data type for the output Series. 
            If not specified, this will be inferred from data. 

        name: str, optional
            The name to give to the Series.
            This will be useful when we need to combine serval series into one dataframe.

        (optional)copy: bool, default False
                      Copy input data. Only affects Series or 1d ndarray input. See examples.

For details:
    https://pandas.pydata.org/docs/reference/api/pandas.Series.html
"""
##
lis_1 = [1 ,2, 3]
dic_1 = {'a': [1,2,3],
         'b': [4,5,6],
         'c': [7,8,9]}
s_lis = pd.Series(lis_1)
s_lis_inde = pd.Series(lis_1, index=['a', 'b', 'c'])
s_lis_inde_name = pd.Series(lis_1, index=['a', 'b', 'c'], name='Series_lis')
s_dic = pd.Series(dic_1)
s_dic_2 = pd.Series(dic_1, 
                    index=['a','e','f'],
                    name='s_dic_2')

#%% Series: Attributes
"""
    1. Series.hasnans:
        Return True if there are any NaNs.
    2. Series.index
    3. Series.is_unique
    4. Series.name
    5. Series.ndim ------> for series, always 1
    6. Series.shape -------> for series, always (n,)
    7. Series.size:
        How many total items in the Series
    8. Series.values 
"""
dic_1 = {'a': [1,2,3],
         'b': [4,5,6],
         'c': [7,8,9]}
s_dic = pd.Series(dic_1)
s_1 = pd.Series([1,2,3], index=['a','b','c'], name='s_1')
s_2 = pd.Series([1,2,np.nan, 4], index=['a','b','c','d'], name='s_2')
s_3 = pd.Series([1,2,np.nan,2], index=['a','b','c','d'], name='s_3')

s_1.hasnans
s_2.hasnans

s_2.is_unique
s_3.is_unique

s_3.name

s_3.ndim

s_3.shape

s_3.size
s_dic.size

s_3.values

s_3.index

#%% Series: Methods
"""
    1. Series.abs(): 
        Return a Series/DataFrame with absolute numeric value of each element.
        Only applies to elements that are all numeric.
        
    2. Series.add(other, 
                  fill_value=None, 
                  axis=0):
        Return series + other
        Add two series by maching the index, if not matched, use fill_value to substitute that missings.
        When fill_value is not provide, i.e. None, Nan is used.
        
    3. Series.add_prefix(str):
        Add str to the start of every index as a prefix.
        
    4. Series.add_suffix(str):
        Add str to the end of every index as a suffix.
        
    5. Series.agg(func=None) = Series.aggregate(func=None): 
        Apply one func(function) or a list of functions to the whole Series not each value.
        Some built-in aggregate func: (we can write our own, see example)
            'mean'
            'sum'
            'size'
            'count'
            'std'
            'var'
            'sem' -----> standard error
            'describe' ----> descriptive statistics (count, mean, std, min, qauntiles(25/50/75), max)
            'first'
            'last'
            'min'
            'max'
    
    6. Series.apply(func, args=())
        Apply function to "every value inside the series" not to the whole seies.
        func: Functoin to be applied to each value.
        args: The others position arguments the function needs.
            PS: Each value of the series should always be the first argument of the function.
   
    7. Series.align(other, 
                    join='outer',
                    fill_value=None, 
                    method=None)
        Use to make two series into one same shape (either outer or inner).
        other: 
            DataFrame or Series
        join:
            {‘outer’, ‘inner’, ‘left’, ‘right’}, default ‘outer’
        fill_value: 
            Value to use for missing values. 
            Defaults to np.nan.
        method: 
            {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None
            Method to use for filling holes in reindexed Series.
            PS:
                pad / ffill: Use lAST valid observation to fill gap.
                backfill / bfill: use NEXT valid observation to fill gap.
    
        PS: append is not working after 1.4.0
    
    
    8. Series.argmax()
        Return position of the maximum value.
    
    9. Serise.argmin()
        Return position of the minimum value.
    
    10. Series.asfreq(freq, method=None, fill_value=None)
        Convert time series to specified frequency.
    
    11. Series.at_time(time)
        Select values at particular time of day (e.g., 9:30AM), including all days has this time.
    
    12. Series.autocorr(lag=1)
        Compute the lag-N autocorrelation.
    
    13. Series.between(left, right, inclusive='both')
        
"""

a = pd.Series([1,2,3], index=['a','b','c'])
b = pd.Series([4,5,6,7], index=['a','b','c','d'])
c = a.add(b, axis=0)
c = a + b
d = a.add(b, axis=0, fill_value=-1)

s = pd.Series([1, 2, 3, 4])
s.add_prefix('row_')

s = pd.Series([1, 2, 3, 4])
s.add_suffix('th_row')

s = pd.Series([1, 2, 3, 4])
s.agg(func='mean')
s.agg(func=['min', 'max', 'mean'])
def MAX_MIN_MEAN(s):
    return s.max()+s.min()+s.mean()
s.agg(fun=MAX_MIN_MEAN)
def multi_return(s):
    return s.max()+s.min(), s.min()+s.mean()
s.agg(fun=multi_return)


#%% Pandas: DataFrame
"""
Two-dimensional, size-mutable, potentially heterogeneous tabular data.
The DataFrame has both a row and column index

Construction:
    pandas.DataFrame(data=None, 
                     index=None, 
                     columns=None, 
                     dtype=None, 
                     copy=None)
    See apendix
    https://pandas.pydata.org/docs/reference/frame.html#attributes-and-underlying-data
"""
# list of list ------> row
lis_lis = [[1,2,3],
           [4,5,6],
           [7,8,9]]
df_lis_lis = pd.DataFrame(lis_lis)

# list of Series ------> row
s_1 = pd.Series([1,2,3], index=['a','b','c'], name='s_1')
s_2 = pd.Series([4,5,6], index=['a','b','c'], name='s_2')
s_3 = pd.Series([7,8,9], index=['a','b','c'], name='s_3')
df_lis_ser = pd.DataFrame([s_1,s_2,s_3])

# dictionary of lis ------> column
dic_lis = {'a':[1,2,3],
           'b':[4,5,6],
           'c':[7,8,9]}
df_dic_lis = pd.DataFrame(dic_lis)

# dictionary of series ------> column
dic_ser = {'s_1': s_1,
           's_2': s_2,
           's_3': s_3}
df_dic_ser = pd.DataFrame(dic_ser)

# dictionary of dictionary 
dic_dic = {'c_1': {'r_1':1, 'r_2':4, 'r_3':7},
           'c_2': {'r_1':2, 'r_2':5, 'r_3':8},
           'c_3': {'r_1':3, 'r_2':6, 'r_3':9}}
df_dic_dic = pd.DataFrame(dic_dic)

#%% DataFrame: Attributes
"""
    1. df.index
    2. df.columns
    3. df.axes
    4. df.values
    5. df.size
    6. df.shape
    7. df.ndim
    8. df.T (transpose)
"""

s_1 = pd.Series([1,2,3], index=['a','b','c'], name='s_1')
s_2 = pd.Series([4,5,6], index=['a','b','c'], name='s_2')
df = pd.DataFrame([s_1,s_2])
df.index
df.columns
df.axes
df.values
df.size
df.shape
df.ndim

#%% Pandas: Index
# 1. reindex
"""
    DataFrame.reindex(newindex, 
                      axis=None, 
                      method=None, 
                      level=None, 
                      fill_value=nan, 
                      limit=None)
"""
df_1 = pd.DataFrame([[1,2,3],
                     [4,5,6],
                     [7,8,9]],
                     index=['r_1', 'r_2', 'r_3'],
                     columns=['c_1', 'c_2', 'c_3'])
new_index = ['r_1', 'x_1', 'x_2', 'r_2']
new_columns = ['c_1', 'y_1', 'c_3']
df_2 = df_1.reindex(new_index, axis=0)#method='nearest')



# 2. rename index
"""
    1. df.index = newindex
       df.columns = newcolumn
    2. df.set_axis(newindex/newcolumn, axis=0/1, inplace=False)
    3. df.rename(dic, axis=0/1, inplace=False)
"""
s_1 = pd.Series([1,2,3], index=['a','b','c'], name='s_1')
s_2 = pd.Series([4,5,6], index=['a','b','c'], name='s_2')
df = pd.DataFrame([s_1,s_2])

df.index = ['s_3', 's_4']

df.set_axis(['s_3', 's_4'], axis=0, inplace=True)

df.rename({'s_1':'s_3'},axis=0, inplace=True)
df.rename(index={'s_1':'s_3'}, columns={'a':'A'}, inplace=True)

#%% Pandas: Data Preprocessing
# 1. Indexing, Slicing, Iterating
"""
    1. loc[:]
    2. iloc[:] ------> integer
    3. at[:]
    4. iat[:] -------> integer
    5. [:]
    6. head(n=5)
    7. tail(n=5)
    8. items()
    9. iteritems() ------> columns base
    10. iterrows() ------> row base
"""
df_1 = pd.DataFrame([[1,2,3],
                     [4,5,6],
                     [7,8,9]],
                    index=['r_1', 'r_2', 'r_3'],
                    columns=['c_1', 'c_2', 'c_3'])

df_1.iloc[0:2, 1:]
df_1.iloc[0,:]

df_1.loc[['r_1','r_3'] ,['c_1','c_2']]
df_1.loc['r_1':'r_2' ,'c_1':'c_2']

df_1.at['r_1','c_2']

df_1.iat[0,1] == df_1.iloc[0,1]

df_1['c_1']
df_1[['c_1','c_3']]
df_1[0:1]

s_1[0:3]
s_1['a':'d']
s_1.loc['a':'d']
s_1.iloc[0:3]


df_2 = pd.DataFrame([[1,2,3],
                     [4,5,6],
                     [7,8,9]])
df_2.iloc[0:2, 0:2]
df_2.loc[0:2, 0:2]


df_1.head(2)
df_1.tail(2)

# 1.1 Other Indexing: Boolean Indexing
"""
    1. Series[boolean expression]
    2. Series.loc[boolean expression]
    3. DataFrame[boolean expression for row]
    4. DataFrame.loc[boolean expression for row, boolean expression for column]
"""
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
s_1 = pd.Series([1,2,3,4,5],
                index = index)
df_1 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]],
                    index = index,
                    columns = col)
s_boo = s_1[[True, False, False, True, True]]
s_boo = s_1.loc[[True, False, False, True, True]]

df_3 = df_1[[True, True, True, False, False]]
df_3 = df_1[df_1['c1']<15]

df_4 = df_1.loc[[True, True, True, False, False], [True, True, True, False, False]]
df_5 = df_1.loc[df_1['c1']<10, df_1['d']<19]


# 2. Summarizing and Computing Descriptive Statistics
"""
for dataframe, 'axis' need to be assigned, either 0 or 1.
    1. sum()
    2. mean()
    3. median()
    4. prod() ------> 連乘
    5. var()
    6. std()
    7. diff() -------> 前者差距
    8. pct_change()
    3. idxmax(), idxmin()
    4. argmax(), argmin()
    5. describe()
    5. count()
    6. abs()
    7. corr()
    8. cov()
    9. min()
    10. max()
    11. mode()
    12. nunique()
    13. value_counts()
    14. info()
"""
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]],
                    index = index,
                    columns = col)
s_2 = pd.Series([1, 2, 3, 4, 5], index=index)

df_2.sum() == df_2.sum(axis=0)
df_2.sum(axis=1)

# 3. Mapping/Repeating functions on iitems or entire series
"""
    1. Series.map(arg, 
                  na_action=None):
        arg: function, collections.abc.Mapping subclass or Series
             Mapping correspondence.
        na_action: {None, ‘ignore’}, default None
             If ‘ignore’, propagate NaN values, without passing them to the mapping correspondence.
        --------> element based on Series
    
    2. DataFrame.apply(func, 
                       axis=0, 
                       **kwargs)
        --------> row/column based on DataFrame
    
    3. DataFrame.applymap(func, 
                          na_action=None, 
                          **kwargs)
        --------> element based on DataFrame
    
"""

scores = pd.Series([90, 65, 40, 80, 75], index=['a','b','c','d','e'])
## squart * 10 
def score_trans(x):
    y = x**0.5 * 10
    return y
## 法一: for loop
new_scores = []
for i in scores:
    new_scores.append(score_trans(i))
new_scores = pd.Series(new_scores, index=scores.index)
## 法二: Series.map()
new_scores_map = scores.map(score_trans)
## 法二.二: lambda
new_scores_lam = scores.map(lambda x: x**0.5*10 )

## apply
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]],
                    index = index,
                    columns = col)
## 法一: for loop
result = []
def trans(col):
    return (col.max()-col.min())/col.mean()
for col_name, col in df_2.items():
    result.append(trans(col))
result = pd.Series(result, index=df_2.columns)

## 法二: DataFrame.apply()
result_apply = df_2.apply(trans, axis=0)

## 法二.二: lambda
result_lamp = df_2.apply(lambda x: (x.max()-x.min())/x.mean(), axis=0)


## applymap
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]],
                    index = index,
                    columns = col)

## 法一: for loop

## 法二: DataFrame.applymap()
def trans(x):
    return x*(-1) + 10
result_applymap = df_2.applymap(trans)
## 法二.二: lambda
result_lam = df_2.applymap(lambda x: x*(-1)+10)









# 4. Droping entire row or column
"""
    1. drop(labels=None, 
            axis=0, 
            level=None, 
            inplace=False)
"""
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]],
                    index = index,
                    columns = col)
df_2 = df_2.drop('c1', axis=1)
df_2.drop('c1', axis=1, inplace=True)
df_2.drop(['c1','c3','c4'], axis=1, inplace=True)
df_2.drop(['a','b'], axis=0, inplace=True)

# 5. Missing Values: Check, Count, Drop, Impute 
"""
    1. isnull()
    2. notnull()
    3. dropna(axis=0/1, 
              how='any'/'all', 
              thresh=None, 
              inplace=False,
              subset=None)
    4. fillna(value=None, 
              method={‘bfill’, ‘ffill’, None}, 
              axis=None, 
              inplace=False, 
              limit=None)
"""
s = pd.Series([1,np.nan,2])
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, np.nan, 3, np.nan, 5],
                     [6, 7, 8, 9, 10],
                     [11,np.nan,13,np.nan,15],
                     [16,17,18,19,20],
                     [21,np.nan,np.nan,24,np.nan]],
                    index = index,
                    columns = col)
df_2_drop = df_2.dropna(axis=0, thresh=2, subset=['c2', 'c3'])
df_2_fill = df_2.fillna()

## fillna---->mean()
fill_dic = {'c1':df_2['c1'].mean(),
            'c2':df_2['c2'].mean(),
            'c3':df_2['c3'].mean(),
            'c4':df_2['c4'].mean(),
            'c5':df_2['c5'].mean()}
df_2_fillmean = df_2.fillna(value=fill_dic, axis=1)

# 6. Duplicate: Check, drop ------> row
"""
    1. duplicated(subset=None, 
                  keep={‘first’, ‘last’})
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html?highlight=duplicated#pandas.DataFrame.duplicated
    2. drop_duplicated(subset=None, 
                       keep={‘first’, ‘last’}, 
                       inplace=False, 
                       ignore_index=False)
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html?highlight=drop_duplicated
"""
# 7. Replacing values: replace, map
"""
    1. replace(to_replace, 
               value, 
               inplace=False,
               regex=False, 
               method={‘ffill’, ‘bfill’, None})
    
    2. with map/applymap method
"""
index = ['a', 'b', 'c', 'd', 'e']
col = ['c1','c2','c3','c4', 'c5']
df_2 = pd.DataFrame([[1, 2, 3, 4, 5],
                     [1, 7, 3, 9, 10],
                     [1,12,3,14,15],
                     [1,17,3,19,20],
                     [1,22,3,24,25]],
                    index = index,
                    columns = col)
df_2_replace_1 = df_2.replace(1, 'missing')
df_2_replace_multi = df_2.replace({1:'miss_1',
                                   3:'miss_3',
                                   12:'miss_12'})

# 8. One-Hot Encoding: get_dummies
"""
    pd.get_dummies(data, 
                   prefix=None, 
                   prefix_sep='_', 
                   dummy_na=False, 
                   columns=None, 
                   drop_first=False)
"""
df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})
df_dumy = pd.get_dummies(df,
                         prefix=["A","B"],
                         prefix_sep='_',
                         columns=['A','B'],
                         drop_first=True)
# 9. Discretization and Binning: cut, qcut
"""
    1. pd.cut(x, 
              bins, 
              right=True, 
              labels=None, 
              precision=3)
    
    2. pd.qcut(x, 
               q, 
               labels=None,  
               precision=3)
"""

#%% Data Manipulation
# 1.Join: merge, join
"""
    pd.merge(df_1, df_2,
             how='inner', 
             on=None, 
             left_on=None, 
             right_on=None, 
             left_index=False, 
             right_index=False, 
             suffixes=('_x', '_y'))
    https://pandas.pydata.org/docs/reference/api/pandas.merge.html?highlight=merge#pandas.merge
    
    df_1.merge(df_2, 
               how='inner', 
               on=None, 
               left_on=None, 
               right_on=None, 
               left_index=False, 
               right_index=False, 
               suffixes=('_x', '_y'))
    
    df_1.join(others, 
              on=None, 
              how='left', 
              lsuffix='', 
              rsuffix='')
    == df_1.merge(df_2, left_index=True, right_index=True)
    
    df_1.join([df_2,df_3,......,df_n], how='inner')
    
"""
# 2.Combine: cocnat, combine_first
"""
    pd.concat(objs,    [df_1,df_2,series_1]
              axis=0, 
              ignore_index=False,
              levels=None)
    
    df_1.combine_first(df_2)  ------> Update
        Update null elements with value in the same location in other.
"""

