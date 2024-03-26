# -*- coding: utf-8 -*-

#%% 0.1 Operator
"""
Arithmetic:
    +
    -
    *
    /
    %
    **
    //
"""

"""
Comparison:
    >
    >=
    <
    <=
    ==
    != (<>)
"""
a = 1
a == 1
"""
Assignment:
    =
    +=:
        c+=a -----> c = c + a
    -=:
        c-=a -----> c = c - a
    *=:
        c*=a -----> c = c * a
    /=:
        c/=a -----> c = c / a
    %=:
        c%=a -----> c = c % a
    **=:
        c**=a ----> c = c ** a
    //=:
        c//=a ----> c = c // a
"""

"""
Identity:
    is
    is not
"""
a is None
import numpy as np
a is np.nan
"""
Membership:
    in
    not in
"""
# e.g.
'a' in ['a',1,2]
'a' not in ['a',1,2]

"""
Logical:
    and (&)
    or (|)
    not
--------------------------------------- 

 "and" | True  | False
---------------------
 True  | True  | False
----------------------
 False | False | False

---------------------------------------

 "or"  | True  | False
---------------------
 True  | True  | True
----------------------
 False | True | False

"""


#%% 1.1 If Elif Else
"""
Structure:
    
If expression_1 :
    .....
elif expression_2 :
    .....
    .....
elif expression_3 :
    .....
    .....
elif expression_4 :
    .....
    .....
else:
    .....
"""

#%% 2.1 Loop: While
"""
When you want to repeat one process until some cretieria is not fulfill(False).
You don't know how many times you want to repeat, use while loop.
Infinite looping if you don't ask it to stop or expression is always true.

Structure:
while expression:
    .....
    .....
else:
    .....
    .....
"""
#e.g.
count = 0
while count < 5:
    print('In while loop: ', count)
    count += 1
else:
    print('In else: ',count)
count += 1
print('Out of while: ', count)

#--------------------------------------#
count = 0
while count < 5:
    print('In while loop: ', count)
    count += 1
    if count >= 3:
        print('In if: ', count)
        break
else:
    print('In else: ',count)
count += 1
print('Out of while: ', count)

#--------------------------------------#
count = 0
while count < 5:
    print('In while loop: ', count)
    count += 1
count += 1
print('Out of while: ', count)

#%% 2.2 Loop: For
"""
Iterate over the iterable object.
Stop when all item is iterated or manually stoped by users.
The iterating times is known.

Structure:
For var in iterable:
    .....
    .....
else:
    .....
    .....
"""
"""
iterable cound be:
    1. string: character
    2. list
    3. tuple
    4. dictionary: key
    5. set
    6. numpy arrary: value
    7. pandas series: value
    8. pandas dataframe: column name
"""
#e.g.1.1
count = 0
for i in ['a','b','c','d','e']:
    print(i)
    print("Times: ", count)
    count += 1
#e.g.1.2
for ind, val in enumerate(['a','b','c','d','e']):
    print(ind, val)
#e.g.2.1
for i in {'key_1':1,
          'key_2':2,
          'key_3':3}:
    print(i)
#e.g.2.2
for key, value in {'key_1':1,
                   'key_2':2,
                   'key_3':3}.items():
    print(key, value)
    
#e.g.2.3
for value in {'key_1':1,
              'key_2':2,
              'key_3':3}.values():
    print(value)

#e.g.3
for char in 'apple':
    print(char)
    
for ind,char in enumerate('apple'):
    print(ind,char)
#e.g.4
import pandas as pd
for i in pd.Series([1,2,3], index=['ind_1', 'ind_2', 'ind_3']):
    print(i)
#e.g.5
import pandas as pd
for i in pd.DataFrame([[1,2,3],[4,5,6], [7,8,9]], 
                      index=['row_1', 'row_2', 'row_3'], 
                      columns=['col_1', 'col_2', 'col_3']):
    print(i)
    
#%% 2.3 Loop: Control
"""
pass:
    do nothing
continue:
    go to the next iteration
break:
    manually exit the loop
"""
#e.g.
for i in range(1,101):
    if i%2 == 0:  #even
        print(i)
        continue
    elif i > 30:
        print("Stop, because {}>30".format(i))
        break
    else:
        pass
print("For Loop ends.")

#%% 4.1 Function
"""
Given inputs and doing some processes, and generate outputs(optional)
When one process would be use multiple times, 
    we can make it a "function" and call it.
All the variables you assigned in the function definition will be created temporary,
    and be deleted when the function is over.

Define a function:
def function_name(inputs):
    ......
    ......
    ......
    return xxx,yyy,zzz #------> return is optional, if you want to output something, return it.
Call a function:
function_name(inputs)
x,y,z = function_name(inputs)
"""
#e.g.1 return the distance between two points
def dis_cal(a,b):
    dis = 0
    for i in range(len(a)):
        dis += (a[i]-b[i])**2
    return dis**0.5
a = (1,2,3,4,5)
b = (5,4,3,2,1)
dis_ab = dis_cal(a, b)


#%% 4.2 Function: inputs
"""
There are four types of inputs can be used:
    1. position:
        use the position(order) of inputs to assign them
    2. keyword:
        assign inputs directly by '='
    3. *:
        change the length changeable input into a tuple, and assign them by position. 
    4. **:
        change the input into a dictionary
"""
#e.g.1 postion & keyword
def sum_all(a,b,c,d,e):
    res = a+b+c+d+e
    return res
s_pos = sum_all(1, 2, 3, 4, 5)
s_key = sum_all(e=5, a=1, c=3, b=2, d=4)

#e.g.2 *
def sum_all_star(*c):
    print('Type of c: ', type(c))
    print('c: ', c)
    res = sum(c)
    return res
s_star = sum_all_star(1, 2, 3, 4, 5)

def sum_all_star_inv(a,b,c,d,e):
    res = a + b + c + d + e
    return res
s_star = sum_all_star_inv(*(1, 2, 3, 4, 5))
                         #*[1, 2, 3, 4, 5]
                         #(1,2,3,4,5)   

#e.g.3 **

def sum_all_star2(**c):
    print('Type of c: ', type(c))
    print('c: ', c)
    res = sum(list(c.values()))
    return res
sum_all_star2 = sum_all_star2(key1=3, key2=4, key3=5)
                            #{'key1':3, 'key2':4, 'key3':5}

def sum_all_star2_inv(a,b,c):
    return a+b+c
sum_all_star2 = sum_all_star2_inv(**{'a':1,
                                     'b':2,
                                     'c':3})
                                 #(a=1, b=2, c=3)

#%% 4.3 Function: global, local, nonlocal
"""
The variables inside and outside the function have no connection, 
    which meas you have no accesses to chage or view variables outside the function when inside the function, vice versa.
The words "global", or 'nonlocal' give you the access.

golbal:
    call in the variable that is not in inputs but outside all the functions. 
    最外層變數
nonlocal:
    call in the variable that is not in inputs but right outside the current function.
    上一層變數
"""
#e.g.1 The furthest outside value cannot be accessed and changed
a = 100
def change_global():
    print(a)
    a = 10
change_global()
print(a)

#e.g.2 Use "global" to get the global value
a = 100 #global variable全域變數
def change_global():
    global a
    print("Before change: ", a)
    a = 10
change_global()
print("After change: ", a)

#e.g.2.1
a = 100 #global variable全域變數
def change_global(a):
    print("Before change: ", a)
    a = 10
    return a
a = change_global(a)
print("After change: ", a)

#e.g.2.2
fin = 100
ret = 250
adv = 300

def summary_acco(fin_in, ret_in, adv_in,
                  a, b, c):
    fin_new = a + fin_in
    ret_new = b + ret_in
    adv_new = c + adv_in
    return fin_new, ret_new, adv_new
fin, ret, adv = summary_acco(50, 60, 10, fin, ret, adv)

fin = 100
ret = 250
adv = 300
def summary_acco_glo(fin_in, ret_in, adv_in):
    global fin, ret, adv
    fin += fin_in
    ret += ret_in
    adv += adv_in
summary_acco_glo(10,20,30)
print('Fin: ', fin)
print('Ret: ', ret)
print('Adv: ', adv)


#e.g nonlocal
x = 10
def outer():
    x = 100
    def inner():
        x = 1000
    inner()
    print(x)
outer()
print(x)
#------------------
x = 10
def outer():
    x = 100
    def inner():
        nonlocal x
        x = 1000
    inner()
    print(x)
outer()
print(x)

#%% 5.1 Exception
"""
In python, "error", i.e. "exception", is also a object. 
When pytho get a exception, the whole process will stop and throw out the error object.

Below are some common error objects:
    Exception: most of the error can be see as this
    AttributeError
    FileNotFoundError
    IOError
    IndexError
    KeyError
    MemoryError
    NameError
    SyntaxError
    SystemError
    TypeError
    ValueError
    ZeroDivisionError

We can use tyr-except to avoid stoping when getting an error.
Python will try the line in "try" section.
If python get error object, go to corresponding "except" section
No matter if a exception occur, python will go in to the "finally" section.

Structure:
try:
    ......
    ......
except error_object1(optional, can be multiple):
    ......
    ......
except error_object2(optional, can be multiple):
    ......
    ......
finally:
    ......
    ......
"""
#e.g.1.
lis = [1,2,3,4,5] #index should be 0 to 4
for i in range(10):
    try:
        print("The value of index {} is {}".format(i, lis[i]))
    except IndexError:
        print("Index {} out of range.".format(i))
        break
    except KeyError:
        print("key")
        
#e.g.1.1
lis = [1,2,3,4,5] #index should be 0 to 4
for i in range(10):
    try:
        print("The value of index {} is {}".format(i, lis[i]))
    except:
        print("Index {} out of range.".format(i))
        break
#e.g.1.2 We can know what type of error occured(error message)
lis = [1,2,3,4,5] #index should be 0 to 4
for i in range(10):
    try:
        print("The value of index {} is {}".format(i, lis[i]))
    except Exception as e:
        print("Default error message is: \n", e)
        print("Index {} out of range.".format(i))
        break
    
"""
Supplemental Material:
We can define our own error message.
"""
#e.g
lis = [1,2,3,4,5] #index should be 0 to 4
for i in range(10):
    try:
        if i > len(lis)-1:
            raise Exception("Own Error: out of range")
        else:
            print("The value of index {} is {}".format(i, lis[i]))
    except Exception as e:
        print("Error message is: \n", e)
        print("Index {} out of range.".format(i))
        break


