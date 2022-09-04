# -*- coding: utf-8 -*-

import pandas as pd, numpy as np
import yfinance as yf
#%% Heirarchical Indexing
"""
    Every index(including columns and index) in a DataFrame or a Series can have not only one layer.
"""
data = pd.Series(range(9),
                 index=[['a','a','a','b','b','c','c','d','d'],
                        ['x','y','z','x','y','x','y','x','y']])
data['a']
data['b']
data.loc[:,'x']

frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=[['a','a','b','b'],
                            [1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

frame['Ohio']

frame.loc[('a',1):('b',1),'Ohio']

idx = pd.IndexSlice
frame.loc[idx[:, 1], idx[:, "Red"]]


#%% Stack / Unstack
"""
    Stack and Unstack can be used to reduce the dimention of the DataFrame
    When stacking, pandas will drop the nan by default, we can add "dropna=False" to avoid this.
    When unstcking, pandas will auto fill nan values.
"""
data = pd.DataFrame(np.arange(6).reshape((2,3)),
                    index = ['Ohio', 'Colorado'],
                    columns = ['one', 'two', 'three'])
data.index.names = ['state']
data.columns.names = ['number']

data1=data.stack()
data1.unstack()
data1.unstack('state')
data1.unstack(0)
data1.unstack('number')
data1.unstack(1)

data = pd.DataFrame([[1,2,np.nan],
                     [3,np.nan,4]],
                    columns=['a','b','c'],
                    index=['one', 'two'])
data.stack()
data.stack(dropna=False)
data.stack().unstack()
data.stack().unstack(fill_value=-999)

frame = pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=[['a','a','b','b'],
                            [1,2,1,2]],
                     columns=[['Ohio','Ohio','Colorado'],
                              ['Green','Red','Green']])
frame.index.names = ['char', 'label']
frame.columns.names = ['state', 'color']
frame.unstack('char')
frame.unstack('label')
frame.T.unstack('state').T
frame.stack('state')
frame.T.unstack('color').T
frame.stack('state')


#%% pivot / melt
"""
    Similiar to stack and unstack, but can set more thing inside
"""
df = pd.DataFrame({'key':['foo', 'bar', 'baz'],
                   'A': [1,2,3],
                   'B': [4,5,6],
                   'C': [7,8,9]})
melted = pd.melt(df)
melted_2 = pd.melt(df, ['key'])

#stack = df.stack(df.columns)

reshaped = melted_2.pivot('key', 'variable', 'value')
melted_2.set_index(['key', 'variable'], inplace=True)
reshaped_unstack = melted_2.unstack('variable')

reshaped['key'] = reshaped.index
reshaped.index = range(3)
reshaped.reset_index(inplace=True)

reshaped.set_index(['key'], inplace=True)
reshaped.index = reshaped['key']
reshaped.drop(['key'], inplace=True)



df = pd.DataFrame({'key':['foo', 'bar', 'baz'],
                   'A': [1,2,3],
                   'B': [4,5,6],
                   'C': [7,8,9]})
melted = pd.melt(df)
melted_2 = pd.melt(df, ['key'])
melted_2['value_2'] = range(9,0,-1)

reshaped = melted_2.pivot('key', 'variable', 'value')
reshaped = melted_2.pivot('key', 'variable', 'value_2')
reshaped = melted_2.pivot('key', 'variable')

#%% group by
"""
    split-apply-combine
   
Step 1. Grouping(splitting)
    We need to provide "key", the cretiria for grouping, to the goupby function.
    The key can be:
        1. list, array (must be the same length)
        2. columns in the DataFrame
        3. dictionary or series
        4. function
ps: 
    we can use for loop to iterate the grouped result
"""
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)},
                  index=range(1,6))
# groupby list
grouped_lis = df.groupby([1,1,2,2,3])
for key, group in grouped_lis:
    print(key)
    print(group)
    print()


# groupby conlumn
grouped_col = df.groupby('key1')
grouped_col = df.groupby('key1', as_index=False)
grouped_col = df.groupby('key1', as_index=True)
grouped_col2 = df.groupby(['key1','key2'])

# groupby dictionary (use index or columns)
people = pd.DataFrame(np.random.randn(5,5),
                      columns=['a','b','c','d','e'],
                      index=['Joe', 'Steve', 'Wes', 'Jane', 'Julia'])
dic = {'a':'red',
       'b':'red',
       'c':'blue',
       'd':'blue',
       'e':'red',
       'f':'yellow'}
grouped_dic = people.groupby(dic, axis=1)

dic_2 = {'Joe': 'g1', 
         'Steve': 'g1', 
         'Wes': 'g2', 
         'Jane': 'g2', 
         'Julia': 'g3'}
grouped_dic_2 = people.groupby(dic_2, axis=0)

## groupby series
ser = pd.Series(dic)
grouped_ser = people.groupby(ser, axis=1)

ser_2 = pd.Series(dic_2)
grouped_ser_2 = people.groupby(ser_2, axis=0)

# groupby function (use index or columns as inputs of the function)
grouped_fun = people.groupby(len, axis=1)
grouped_fun_2 = people.groupby(len, axis=0)
grouped_fun_title = people.groupby(lambda x: x[0], axis=1)
grouped_fun_title_2 = people.groupby(lambda x: x[0], axis=0)
 


"""  
Step 2. Applying method on every group, and get the result
    We can use some functions already optimized:
        1. count()
        2. sum()
        3. mean()
        4. median()
        5. std(), var()
        6. min(), max()
        7. prod()
        8. fist(), last()
    or all other series or dataframe function:
        1. descripe()
    or any user-defined function, using "apply" and "aggregate"
    We can even apply serval methods on one columns, apply different method on different column, or both.
"""
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)},
                  index=range(1,11))
grouped_key1 = df.groupby('key1')


## Using built-in functions
count_group = grouped_key1.count()
sum_group = grouped_key1.sum()
mean_group = grouped_key1.mean()
prod_group = grouped_key1.prod()
first_group = grouped_key1.first()
last_group = grouped_key1.last()

descr_group = grouped_key1.describe()


## Using user-defined functions: groupby.apply()
"""
When using "groupby.apply(fun)", the input of the function must be a dataframe. 
Pandas will automatically concate the result dataframe from different groups into a big final dataframe.
"""
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)},
                  index=range(1,11))
def top_3(df, n=3, sort_col='data1'):
    return df.sort_values(by=sort_col)[-n:]
def top_n(a, n, sort_col):
    return a.sort_values(by=sort_col)[-n:]

appy_top_3 = df.groupby('key1').apply(top_3)
appy_top_3_noindex = df.groupby('key1').apply(top_3)
appy_top_4 = df.groupby('key1').apply(top_n, n=4, sort_col='data2')

## (Optional) two arguments in groupby: as_index & group_keys
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)},
                  index=range(1,11))
top3_ori = df.groupby('key1').apply(top_3)
top3_AsIndexFalse = df.groupby('key1', as_index=False).apply(top_3)
top3_GroupKeysFalse = df.groupby('key1', group_keys=False).apply(top_3)

## Using user-defined functions: groupby.aggregate(agg)
"""
When using "groupby.agg(fun)", the input of the function must be a list-like object. 
Work just like DataFrame.agg()
Pandas will automatically concate the result dataframe from different groups into a big final dataframe.
"""

## (Supplementary Material) DataFrame.agg()
"""
"DataFrame.agg()" is a enhanced eddition of "DataFrame.apply()". 
When using apply(), we can only apply one function column-by-column or row-by-row, 
    but when using agg(), we can apply serveral funcitons to each column or apply specific functions to specific columns.
"""
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)},
                  index=range(1,11))
df_agg_single = df.agg('mean')
df_agg_multi_1 = df.agg(['mean','sum'])
df_agg_multi_1 = df.agg(['mean', 'sum'])
df_agg_mulit_2 = df.agg({'data1': ['mean','sum','std'],
                         'data2': ['min', 'max']})

## groupby.agg()
df = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a'],
                   'key2':['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)},
                  index=range(1,11))
grouped_agg_0 = df.groupby('key1').agg('mean')
grouped_agg_multi_1 = df.groupby('key1').agg(['mean','sum'])
grouped_agg_multi_1_rename = df.groupby('key1').agg([('group_mean', 'mean'),
                                                     ('group_sum', 'sum')])
grouped_agg_multi_2 = df.groupby('key1').agg({'data1': ['mean','sum','std'],
                                              'data2': ['min', 'max']})

def max_min_avg(ser):
    return (max(ser)-min(ser))/ser.mean()

group_agg_multi_3 = df.groupby('key1').agg({'data1': ['mean','sum','std'],
                                            'data2': ['min', 'max', max_min_avg]})
group_agg_multi_rename = df.groupby('key1').agg({'data1': [('group_mean', 'mean'),
                                                           ('group_sum', 'sum'),
                                                           ('group_std', 'std')],
                                                 'data2': ['min', 'max', max_min_avg]})