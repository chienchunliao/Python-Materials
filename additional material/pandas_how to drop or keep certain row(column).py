# -*- coding: utf-8 -*-
import pandas as pd

#%% df.any(axis)
'''
df.any(axis=0): check the df column by column; 
    if any of the values in the column is "True", it will return "True"
df.any(axis=1): check the df row by row; 
    if any of the values in the row is "True", it will return "True"
'''
df_true_false = pd.DataFrame([[True, False],
                              [False, False],
                              [True, True],
                              [False, True]],
                             index = ['row_1','row_2','row_3','row_4'], 
                             columns = ['col_1', 'col_2'])
print('Original df:\n', df_true_false)
print()

df_any_axis0 = df_true_false.any(axis=0)
print('df.any(axis=0):\n', df_any_axis0)
print()

df_any_axis1 = df_true_false.any(axis=1)
print('df.any(axis=1):\n', df_any_axis1)
print()

#%% df.all()
'''
df.all(axis=0): check the df column by column; 
    if all of the values in the column is "True", it will return "True"
df.all(axis=1): check the df row by row; 
    if all of the values in the row is "True", it will return "True"
'''
df_true_false = pd.DataFrame([[True, False],
                              [False, False],
                              [True, True],
                              [False, True]],
                             index = ['row_1','row_2','row_3','row_4'], 
                             columns = ['col_1', 'col_2'])
print('Original df:\n', df_true_false)
print()

df_any_axis0 = df_true_false.all(axis=0)
print('df.all(axis=0):\n', df_any_axis0)
print()

df_any_axis1 = df_true_false.all(axis=1)
print('df.all(axis=1):\n', df_any_axis1)
print()

#%% Why should we need .any() or .all()
'''
Let's see the df below.
We have 4 task:
    1. drop/keep the row if any of the values in 'col_4' and 'col_5' is 99999
    2. drop/keep the row if all of the values in 'col_4' and 'col_5' are 99999
    3. drop/keep the column if any of the values in 'col_4' and 'col_5' is 99999
    4. drop/keep the column if all of the values in 'col_4' and 'col_5' are 99999
'''


df = pd.DataFrame([[1,2,3,99999,0],
                   [4,5,6,0,99999],
                   [7,8,9,99999,99999],
                   [10,11,12,5000,6000]],
                  columns = ['col_1', 'col_2','col_3', 'col_4', 'col_5'])

## Step 1.
'''
we need to check if the values inside those two columns are 99999
'''
is_99999 = df[['col_4', 'col_5']] == 99999
print(is_99999)
print()

#%% Task 1: drop/keep the row if any of the values in 'col_4' and 'col_5' is 99999 
'''
we need to check the 'is_999999' row by row. 
   If any values on 'col_4' and 'col_5' in the row is 99999, we need to set the row to True.
'''

print('original df: \n',df)
print()

is_99999_by_row_any = is_99999.any(axis=1)
print('check by row (any):\n',is_99999_by_row_any)
print()

'''
Then we can use the True_False series to slice the original df
'''
## Keep the row
df_any_by_row_keep = df.loc[is_99999_by_row_any]
print('After keeping the row (any): \n', df_any_by_row_keep)
print()
## Drop the row
df_any_by_row_drop = df.loc[~is_99999_by_row_any]
print('After droping the row (any): \n', df_any_by_row_drop)
print()

#%% Task 2: drop/keep the row if all of the values in 'col_4' and 'col_5' is 99999 
'''
we need to check the 'is_999999' row by row. 
   If all values on 'col_4' and 'col_5' in the row are 99999, we need to set the row to True.
'''

print('original df: \n',df)
print()

is_99999_by_row_all = is_99999.all(axis=1)
print('check by row (all):\n',is_99999_by_row_all)
print()

'''
Then we can use the True_False series to slice the original df
'''
## Keep the row
df_all_by_row_keep = df.loc[is_99999_by_row_all]
print('After keeping the row (all): \n', df_all_by_row_keep)
print()
## Drop the row
df_all_by_row_drop = df.loc[~is_99999_by_row_all]
print('After droping the row (all): \n', df_all_by_row_drop)
print()

#%% Task 3: drop/keep the column if any of the values in 'col_4' and 'col_5' is 99999 
'''
we need to check the 'is_999999' column by column. 
   If any values in 'col_4' and 'col_5' is 99999, we need to set the column to True.
'''

print('original df: \n',df)
print()

is_99999_by_col_any = is_99999.any(axis=0)
print('check by column (any):\n',is_99999_by_col_any)
print()

'''
Then we can use the True_False series to slice the original df
'''
df_other = df.loc[:, ~df.columns.isin(['col_4', 'col_5'])]


## Keep the column
df_check = df[['col_4', 'col_5']].loc[:,is_99999_by_col_any]
df_any_by_col_keep = pd.concat([df_other, df_check],axis=1)
print('After keeping the column (any): \n', df_any_by_col_keep)
print()
## Drop the column
df_check = df[['col_4', 'col_5']].loc[:,~is_99999_by_col_any]
df_any_by_col_drop = pd.concat([df_other, df_check],axis=1)
print('After droping the column (any): \n', df_any_by_col_drop)
print()

#%% Task 4: drop/keep the column if all of the values in 'col_4' and 'col_5' are 99999 
'''
we need to check the 'is_999999' column by column. 
   If all values in 'col_4' and 'col_5' is 99999, we need to set the column to True.
'''

print('original df: \n',df)
print()

is_99999_by_col_all = is_99999.all(axis=0)
print('check by column (all):\n',is_99999_by_col_all)
print()

'''
Then we can use the True_False series to slice the original df
'''
df_other = df.loc[:, ~df.columns.isin(['col_4', 'col_5'])]


## Keep the column
df_check = df[['col_4', 'col_5']].loc[:,is_99999_by_col_all]
df_all_by_col_keep = pd.concat([df_other, df_check],axis=1)
print('After keeping the column (all): \n', df_all_by_col_keep)
print()
## Drop the column
df_check = df[['col_4', 'col_5']].loc[:,~is_99999_by_col_all]
df_all_by_col_drop = pd.concat([df_other, df_check],axis=1)
print('After droping the column (all): \n', df_all_by_col_drop)
print()





