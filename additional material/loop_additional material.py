# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd

#%% When to use loop
'''
1. when we need to do similiar process repeatly

2. You want to regularly do something following some rules

4. when you need to iterate all the object in a iterable object, 
    e.g. strign, list, dictionay, set, series, dataframe...etc.
    p.s. iterable object: When you can read all the stuff inside the object one by one, 
                          we said the object is iterable.
                          Any python object can be made as a iterable object. (How to achivev it will be discuss in the "Advance Class building" if you are interested)                          
'''


#%% Two type of loop: for, while
'''
1. The times of repeat can be known or unknown
    e.g.
    known:
        a. Repeat 10 times
        b. Repeat over the whole iterable object(strign, list, dictionay, set, series, dataframe...etc.)
    unknown:
        c. Repeat until we tell it to stop
        d. Repeat until some rules are broken

'''
#a. repeat 10 times
for i in range(10):
    print(i)

#b. Repeat over iterable object
## String
for char in 'apple':
    print(char)
## List
for i in [1,2,3]:
    print(i)
## Dictionary  ***Important***
dict_sample = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog', 'f':'fish'}
for key in dict_sample:
    print(key)
for key in dict_sample.keys():
    print(key)
for val in dict_sample.values():
    print(val)
for key, val in dict_sample.items():
    print("{}: {}".format(key, val))
    
## Set
set_sample = {1,2,3,4,5,6,7,8,9}
for obj in set_sample:
    print(obj)
    
## Series   ***Impotant***
ser_sample = pd.Series(data=[1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g'])
for val in ser_sample:
    print(val)
for idx in ser_sample.index:
    print(idx)
for idx,val in ser_sample.items():
    print("{}: {}".format(idx, val))

## DataFrame   ***Important***
df_sample = pd.DataFrame(data=[[1,2,3], [4,5,6], [7,8,9]],
                         index=['row_1', 'row_2','row_3'],
                         columns=['col_1','col_2', 'col_3'])
for col_name in df_sample:
    print(col_name)
for col_name in df_sample.columns:
    print(col_name)
    
for row_name in df_sample.index:
    print(row_name)

for col in df_sample.iteritems():
    print(col)
    print()
    ##each col is a pandas series

for row in df_sample.iterrows():
    print(row)
    print()
    ##each row is a pandas series
    
#c. Repeat until we tell it to stop
key_in = ''
print('Key in anything to start. Key in p to stop.')
while key_in != 'p':
    key_in = input('Please key in: ')
    print('The words you key in: ', key_in)
print('End')

#d. Repeat until some rule is broken
# There are tow way to achiev this:
#     1. while
#     2. for + if + break
## While: 找最小公倍數15,48
numb = 1
while (numb%15 != 0) or (numb%48 != 0):
    numb += 1
print(numb)
## for + if + break: iterate list, 當找到'error'就停
list_1 = [1,2,3,4,'error',6,7]
for i in list_1:
    if i == 'error':
        break
    else:
        print(i)

#%% Useful looping skill

# 1. loop and storage with list: 很常用
data = [1,2,3,4,5,6,7]
result = []
for i in data:
    new = i*5
    result.append(new)
print(result)
    
# 2. loop and storage with dictionary: 很常用
data = ['a','b','c','d','e','f','g']
result = {}
for idx, val in enumerate(data):
    new_key = 'position_' + str(idx)
    new_val = val
    result[new_key] = new_val
print(result)

# 3. loop, storage and update the dictionary: 很常用
## example: count number of values
data = ['a','a','a','b','b','c','c','c','c','d','d','d']
result = {}
for i in data:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)

# 3. loop and storage with series: 用的少
str_sample = 'apple'
pos = 0
result = pd.Series()
for char in str_sample:
    idx = 'position_' + str(pos)
    result[idx] = char
    pos += 1
print(result)

# 4. 跳著取
data = ['a','b','c','d','e','f','g']
for i in data[::2]:
    print(i)
for pos,val in enumerate(data):
    if pos%2 == 0:
        print(val)
    else:
        pass