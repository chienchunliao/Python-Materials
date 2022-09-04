# -*- coding: utf-8 -*-
"""
Define a function:
    input: iterable object (string or list for this practice)
    output: dictionary (key= unique character or element; 
                        vlue= correspending appear times)
    goal: Summary the content(unique character or element) in the iterable object.
          When input type is not iterable, print any error message you define.
          If the input is string, ignore all spaces and uppcase or lowercase but keep all punctuation marks.
    example:
        1. input: [1,1,3,2,2,4,4,4,5]
           ouput: {1:2,
                   2:2,
                   3:1,
                   4:3,
                   5:1}
        2. input: "I have a pen, I have a apple
                   Uh! Apple-Pen!
                   I have a pen, I have pineapple
                   Uh! Pineapple-Pen!"
           output: {'i': 6, 
                    'h': 6, 
                    'a': 11, 
                    'v': 4, 
                    'e': 14, 
                    'p': 14, 
                    'n': 6, 
                    ',': 2, 
                    'l': 4, 
                    '\n': 3, 
                    'u': 2, 
                    '!': 4, 
                    '-': 2}
        3. input: 5
           ouput: "Wrong input type!"

"""
def counters(x):
    try:
        dic = {}                         # constract an empty dictionary
        if type(x) == str:               # to check if the input is sting
            x = x.lower()                #     if the input is string transform all letter into lowercase;
            x = x.replace(' ', '')       #     remove all spaces
        for i in x:
            if i not in dic:             # check whether the element is one of the keys in dictionary
                dic[i] = 1               #     if not, construct a new key-value pair; 
            else:                        #     else(key in the dictionary), add one to the original value
                dic[i] += 1
        return dic
    except Exception as e:               # to catch the error object and print it out
        print("Error Type: {}".format(e))


                
