# -*- coding: utf-8 -*-
import pandas as pd
#%% Combining loop and function
#%% Why we need to combine loop and function
'''
1. We can perform similar task easily by using function. 
    We can do stuff repeatly and regularily by using loop.
    If combing two together, we can easily peform similar task repeatly and regularily.
'''

#%% Two type of loop+function
'''
1. looping outside a function:
    def func():
        ......
        ......
        
    for ...... :
        func()
        
2. looping inside a function: 
    def func(...):
      for ......:
          ....
          ....
          
3. looping inside and outside a function:
    def func(...):
        ....
        ....
        for ..... :
            ....
            ....
    
    for ..... :
        func()
        
'''

#1. looping outside a function:  最常用
def get_word_len_single(string):
    return [string, len(string)]
    
data = ['apple', 'ball', 'cat', 'door']
outcome = []
for i in data:
    outcome.append(get_word_len_single(i))
print(outcome)

#2. looping inside a function:  
def get_word_len_multi(lis):
    result = []
    for string in lis:
        result.append([string, len(string)])
    return result
    
data = ['apple', 'ball', 'cat', 'door']
outcome = get_word_len_multi(data)
print(outcome)

#3. looping inside & outside a function:
def count_char(string):
    result = {}
    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return [string, result]
    
    
data = ['apple', 'ball', 'cat', 'door']
outcome = []
for i in data:
    outcome.append(count_char(i))
print(outcome)
#%% Upgraded loop+function
'''
1. map(func, iterable): 等同於looping outside a function
                        map是python本身的function, 所以適用於所有iterable object
2. Series.apply(func): pandas裡面的map, 
                        等同於looping outside a function. 
                        Each element is the input of the function
3. DataFrame.apply(func, axis): Eache row(axis=1)/column(axis=0) is the input of the function
4. DataFrame.applymap(func): Each cell is the input of the function

'''
##1. map
def get_word_len_single(string):
    return [string, len(string)]

outcome = list(map(get_word_len_single, data))
print(outcome)
#----等同於
data = ['apple', 'ball', 'cat', 'door']
outcome = []
for i in data:
    outcome.append(get_word_len_single(i))
print(outcome)

#2. Series.apply()
def get_word_len_single(string):
    return [string, len(string)]

data = pd.Series(['apple', 'ball', 'cat', 'door'])
outcome = data.apply(get_word_len_single)
print(outcome)
#----等同於
outcome = []
for i in data:
    outcome.append(get_word_len_single(i))
outcome = pd.Series(outcome)
print(outcome)

#3. DataFrame.apply()
def get_max_min(lis):
    return [min(lis), max(lis)]

##axis=1
df = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]],
                  index = ['row_1', 'row_2', 'row_3'],
                  columns = ['col_1', 'col_2', 'col_3'])
outcome = df.apply(get_max_min, axis=1)
print(df)
print(outcome)
#----等同於
outcome = []
for idx, row in df.iterrows():
    outcome.append(get_max_min(row))
outcome = pd.DataFrame(outcome, 
                       index = df.index)
print(df)
print(outcome)

##axis=0
df = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]],
                    index = ['row_1', 'row_2', 'row_3'],
                    columns = ['col_1', 'col_2', 'col_3'])
outcome = df.apply(get_max_min, axis=0)
print(df)
print(outcome)
#----等同於
outcome = []
for col_name, col in df.iteritems():
    outcome.append(get_max_min(col))
outcome = pd.DataFrame(outcome, 
                       index = df.columns).T
print(df)
print(outcome)


#4. DataFrame.applymap(func)
df_C = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]],
                  index = ['row_1', 'row_2', 'row_3'],
                  columns = ['col_1', 'col_2', 'col_3'])
def C_to_F(cell):
    out = cell * 1.8 + 32
    return out
df_F = df_C.applymap(C_to_F)
print(df_F)
#----等同於
df_C = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]],
                  index = ['row_1', 'row_2', 'row_3'],
                  columns = ['col_1', 'col_2', 'col_3'])
df_F = df_C.copy()
for row_idx in range(df_C.shape[0]):
    for col_idx in range(df_C.shape[1]):
        df_F.iat[row_idx, col_idx] = C_to_F(df_C.iat[row_idx, col_idx])

print(df_F)



