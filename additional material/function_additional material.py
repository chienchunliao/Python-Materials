# -*- coding: utf-8 -*-
import pandas as pd
#%% What is a 'function'
'''
1. Function is one kind of process or a group of processes.

2. Function takes ingredients, in programming we called them 'inputs', 
    do something(some processes we have defined when we created the fucntion) on the ingredients, 
    and generate the results, we call them 'outputs'.
    
3. Function can pack a group of process into one process, because sometimes we just don't care some details.
    e.g. 
    When doing standalization, we know that we need to: 
        1. calculate the mean
        2. calculate the standard deviation
        3. calculate z = (x-mean)/std
    It actually contains three steps, but what we really care is the result(z).
    So we can pack the three steps above into one:
        1. calculate z
    The details, how to calculate, we hide them into a function.
    
4. When every process in the function is done, 
    Python will only remember/store the 'outputs' and forget/delete everything you do inside the function.
    
5. We can give function a 'name', any name you want.
    e.g.
    The whole process is standalizing the data; we can call the function 'standarlize'.
'''

#%% How to make/define a 'function'?
'''
def func_name(input):
    .......
    .......
    .......
    return output
'''

#%% How to use/call a 'function'?
'''
output = func_name(input)
'''

#%% When do we need a 'function'?
'''
1. When the process we need to be used more than once.
   No one wants to write the same code for the same process everytime.
   
2. When you want to make your main code section look very clean, concise, and tidy.
'''
"The following two section do the same thing; only to compare the length of the main code section"
#---1. Without function
##-----main code--------
import statistics as st
data_1 = [2,4,6,8,10,12]
data_2 = [1,3,5,7,9,11]

mean_1 = st.mean(data_1)
std_1 = st.stdev(data_1)
result_1 = []
for i in data_1:
    result_1.append((i-mean_1)/std_1)
    
mean_2 = st.mean(data_2)
std_2 = st.stdev(data_2)
result_2 = []
for i in data_2:
    result_2.append((i-mean_2)/std_2)
##-----------------------
    
#---2. With function
import statistics as st
def standarlize(data):
    result = []
    mean = st.mean(data)
    std = st.stdev(data)
    for i in data:
        result.append((i-mean)/std)
    return result
##-----main code--------
data_1 = [2,4,6,8,10,12]
data_2 = [1,3,5,7,9,11]

result_1 = standarlize(data_1)
result_2 = standarlize(data_2)
##----------------------
        

#%% Why do we need a 'function'?
'''
1. To Make code consise, clean, and more readable.

2. To use less memory than without it. 
    As we mentioned, functionn will not storage anything except outputs; 
    so any variable we created or any memory space we used inside the function will be release after the function is finished.

3. Make some frequently used processes easy to access anytime we want them.
    e.g. calculate the standard deviation
'''

#%% Where do we use a 'function'?
'''
1. Where we find out that we keep writing similiar code over and over, convert them into fucntion.

2. Where the details are not important, i.e. only caring about the results, convert it into function.'''