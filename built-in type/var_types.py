 # -*- coding: utf-8 -*-

dir([])
dir('')
dir(5)
[1,3,4]
'apple'

#%% 1.1 Numeric: Integer & Float
"""
Float: Represents the floating point number(decimals). Python float values are represented as 64-bit double-precision values(float64).
"""
#e.g.
int_1 = 10
flo_1 = 1.5

print(type(int_1))
print(type(flo_1))

#%% 1.2 Numeric: Common Operators
"""
    1. +
    2. -
    3. * : Multiplication
    4. ** : Power (e.g. Square root of x ---> x**0.5)
    5. / : Normal division (float) 
    6. //:Floor division
    7. % : Modulus;returns the remainder when the first operand is divided by the second
    
    PS: When int and float are calculated together, the results are mostly float.
"""
2 + 3
2.0 + 3
2.5 + 3.5

2 * 3
2.0 * 3

2 ** 3
2.0 ** 3
2 ** 3.0
4 ** 0.5

8 / 3 
8 // 3

8 % 3

#%% 1.3 Integer & Float: Common Functions
"""
    1. abs(x): 
        Return the absolute value of x
    2. int(x): 
        Conver x to integer
    3. float(x): 
        Conver x to float 
    4. divmod(x, y): 
        Display the quotient and the remainder(in a tuple) of x divided by y
    5. pow(x,y): 
        Equal to x**y
    6. round(x, n): 
        Return a float number that will be rounded to the n decimal places. If n is not given, the default is 0 decimal place.
"""
abs(-1)

int(5)
int(1.2)

float(2.3)
float(2)

divmod(8, 3)

pow(2, 3)

round(1.5)
round(2.5)
round(1.51, 1)
round(1.65, 1)

#-------------------------------------------------------------------------------------------------------------
"""
常見 methods: (optional)
    1. x.is_integer(): 
        Return True when x is integer
    2. x.as_integer_ratio(): 
        Returns a pair of integers whose ratio is exactly equal to the original float and with a positive denominator
"""
1.5.is_integer()
1.5.as_integer_ratio()
#%% 1.4 數學常用package補充: math
"""
    1. math.pi: 
        3.14159......
    2. math.e: 
        2.71828......
    3. math.fabs(x): 
        abs(x)
    4. math.floor(x): 
        Rounds down and returns the largest integer less than or equal to a given number
    5. math.ceil(x): 
        Rounds up and returns the smallest integer greater than or equal to a given number
    6. math.factorial(x): 
        math.factorial(x) = x! 
                          = 1*2*3*....*(x-1)*x
    7. math.log(x, y): 
        Return the logarithm of x to base y. If y is not given, return the natural logarithm of x
    8. math.pow(x, y): 
        x**y
    9. math.sqrt(x): 
        x**0.5
    10. math.sin()
        math.cos()
        math.tan()
        math.asin()
        math.acos()
        math.atan()
"""
import math
math.pi
math.e
math.fabs(-15)
math.floor(98.6)
math.floor(-271.1)
math.ceil(98.6)
math.ceil(-271.1)
math.factorial(5)
math.log(8)
math.log(8, 2)
math.sqrt(4)


#%% 2.1 Text Sequence Type: String
"""
String is immutable.
' ' or " " or 
''' ''' or """ """ (more than one lines)
"""
#e.g.
'a'
"apple"
"I did nothing."

#%% 2.2 String: Getting substring & Slicing & Modifing
"""
    1. s[a]: 
        return the character on position a of string s
        PS: Python will raise error if out of bounds.
    2. s[a:b:c]: 
        return objects starting from position a, ending at position b(excluded), and stepping c in string s.
        PS: Python will not raise error if out of bounds; it will just return nothing.
    3. s1 + s2 +.....:
        Combine strings 
    4. s1 * k:
        Repeating s1 k times.
"""
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[3]
letters[-3]
letters[100] #------> error "index out of range"
letters[:]
letters[10:]
letters[12:15]
letters[12:-3]
letters[::2]
letters[12:20:3]
letters[::-1]
letters[22:100] #-----> "xyz"
letters[100:] #------> ""
letters * 2
letters + '12345'

#%% 2.3 String: Escaspe Character(\*)
"""
    1. \': string內的'
    2. \": string內的"
    3. \\: string內的\
    4. \b: BackSpace
    5. \n: 換行
    6. \r: 游標移到最左邊 
    7. \t: Tab鍵
    8. \f: 換頁
or using: r' '
"""
print("ABC\'D")
print("ABC\"D")
print("ABC\\D")
print("ABC\bD")
print("ABC\nD")
print("ABC\rD")
print("ABC\tD")

#%% 2.4 String: Common Functions
"""
    1. len(s):
        Number of characters including space
    2. sorted(s, key, reverse=False):
        Return a list
    3. enumerate(s)
    4. zip([s1, s2, s3,......])
"""
len("ABCD")
sorted("CADB")
zip("ABCD", "1234", "wxyz")
for position, char in 'apple':
    print("The character on position {} is {}".format(position, char))

#%% 2.5 String: Common Methods
"""
Type help(str.*) in terminal to see the details of each method
    1. s.find(x, [start, end]): 
        Return first index of x in s from position start to end. 
        Return -1 if x is not found.
    2. s.rfind(x): 
        Return the last index of x. 
        Return -1 if x is not found.
    3. s.index(x, [start, end]): 
        Return first index of x in s from position start to end. 
        Raise ValueError if x is not found.
    4. s.rindex(x): 
        Return last index of x in s from position start to end. 
        Raise ValueError if x is not found.
    5. s.replace(old, new[, count]): 
        Replace old with new for many times.
        Returns a copy of the string.
        If count is not given, replace all matched. 
    6. s.split(sep[, maxsplit]):
        Returns a list of the words in the string, separated by the sep string. 
        Default maxsplit=-1, meaning seperate all.
    7. s.join(l):
        Join elements in l by s. Returns a string.
    8. s.lstrip(x):
        切頭, 只要有就去掉
        default 刪除所有空白
    9. s.removeprefix():
        切頭, 只切一次
    10. s.rstrip(x):
        切尾, 只要有就去掉
    11. s.rsplit(sep[, maxsplit]):
        右邊開使版本的split         
    12. s.upper():
        全大寫
    13. s.lower():
        全小寫
    14. s.capitalize():
        字首大寫
    15. s.title():
        所有字首大寫
    16. s.swapcase():
        大小寫對調
    17. s.startswith(x):
        Return True when s is started with x.
    18. s.endswith(x):
        Return True when s is ended with x.
    19. s.format()
"""
#1. find
"ABAB".find("B")
"ABAB".find("B", 2)
"ABAB".find("B", 5) #-----> -1
"ABAB".find("C") #----> -1

#2. rfind
"ABAB".rfind("B")

#3. index
"ABAB".index("B")
"ABAB".index("B", 2)
"ABAB".index("B", 5) #----> error "substring not found"
"ABAB".index("C") #----> error "substring not found"

#4. rindex
"ABAB".rindex("B")

#5. replace
"A*B*C*D".replace('*', '+')
"A*B*C*D".replace('*', '+', 2)

#6. split
"A*B*C*D".split('*')
"A*B*C*D".split('*', 2)

#7. join
'*'.join(['A','B','C','D'])

#8. lstrip
"ABABCDEF".lstrip('B')
"ABABCDEF".lstrip('AB')

#9. removeprefix
'Arthur: three!'.lstrip('Arthur: ')
'Arthur: three!'.removeprefix('Arthur: ')

#10. rstrip
"ABABCDEFFE".rstrip('E')
"ABABCDEFFE".rstrip('EF')

#11. upper
"abcd".upper()

#12. lower
"ABCD".lower()

#13. capitalize
"abcd".capitalize()

#14. title 
"the university of texas at dallas".title()

#15. swapcase
"AbCd".swapcase()

#16. startswith
"ABCD".startswith("A")
"ABCD".startswith("B")

#17. endswith
"ABCD".endswith("D")
"ABCD".endswith("B")

#18. format

"Today is {}-{}-{}".format(2022, 5, 16)
"Today is {y}-{m}-{d}".format(y = 2022, m = 5, d = 16)
"Today is {2}-{0}-{1}".format(5, 16, 2022)
"Today is {2}-{0}-{1}".format(*[5, 16, 2022])


#%% 3.1 Sequence Types: List
"""
Mutable: List []
ordered
"""
#e.g.
[1,2,3]
[1, 'a', 2.0, 'b', True]
[[1, 2], [3, 4], [5, 6]]

#%% 3.2 List: Getting Elements & Slicing & Modifing values
"""
    1. l[x]: 
        Return the object on position x.
        ~超出範圍會 raise error
    2. l[a:b:c]: 
        Return iterable(a copy) starting from position a, 
            ending at position b(excluded), and stepping c.
        The original iterable will not changed.
        ~超出範圍不error, 會return empty
    3. l[k] = x:
        把 position k 的 element 改成 x
    4. l1 + l2:
        concat l1 and l2
    5. l1 * n:
        repeat n times
"""
#1. get elements
['a','b','c'][0]
['a','b','c'][4] #----> error
['a','b','c'][-1]
['a','b','c'][-2]
a, b, c = ['a', 'b', 'c']
a, b, c = ['a', 'b', 'c', 'd', 'e']
a, b, *c = ['a', 'b', 'c', 'd', 'e']
a, *b, c = ['a', 'b', 'c', 'd', 'e']
*a, b, c = ['a', 'b', 'c', 'd', 'e']

#2. slice
['a','b','c', 'd', 'e'][1:3:2]
['a','b','c', 'd', 'e'][1:3:-1]
['a','b','c', 'd', 'e'][:3]
['a','b','c', 'd', 'e'][1:]
['a','b','c', 'd', 'e'][::-1]
['a','b','c', 'd', 'e'][:]

#3. modify
['a','b','c', 'd', 'e'][1] = 5
['a','b','c', 'd', 'e'][1:3] = [1, 2]
lis = [25,26,30]

#4. +
[1, 2, 3] + [4, 5, 6]
['a','b','c'] + [1, 2, 3]
## Cannnot apply '-' to two lists. 
##     e.g.[1, 2, 3] - [2, 3]

#5. *
[1, 2, 3] * 2
['a','b','c'] * 2

#%% 3.3 List: Common Functions
"""
    1. enumerate(l)
    2. len(l):
        Count the number of elements in the list.
    3. min(l):
        Return the minimium value in list.
    4. max(l):
        Return the maximium value in the list.
    5. sum(l):
        Return the summation of the list.
    6. zip([l1,l2,l3,......])
    7. sorted(iterable, key, reverse=False):
        Return a sorted list.
        The original list will not change.
        reverse=False ------> 由小到大
        reverse=True  ------> 由大到小
        key: the sorting creteria ------> usually use "lambda"
        
    
"""
#1. enumerate
for position, element in enumerate(['a', 'b', 'c', 'd']):
    print("The element in position {} is {}".format(position, element))

#2. len
len([1, 2, 3])

#3. min
min([1, 2, 3])

#4. max
max([1, 2, 3])

#5. sum
sum([1, 2, 3])

#6. zip
list(zip(['a','b','c'], [1,2,3], ['x','y','z']))

#7. sorted
l = [5,4,1,2,3]
l_sorted = sorted(l)
l_sorted_rev = sorted(l, reverse=True)

l1 = [['a', 4], ['c', 2], ['d', 1], ['b', 3]]
l1_by_char = sorted(l1, key=lambda x:x[0])
l1_by_char_rev = sorted(l1, key=lambda x:x[0], reverse=True)
l1_by_numb = sorted(l1, key=lambda x:x[1])
l1_by_numb_rev = sorted(l1, key=lambda x:x[1], reverse=True)

#%% 3.4 List: Common Methods
"""
Type help(list.*) in terminal to see the details of each method
    1. l.clear():
        empty the list
    2. l.append(x):
        add x to the end of list
    3. l1.extend(l2): 
        the same as "l1 += l2"
    4. l.insert(k, x):
        Insert x in position k, others move back one position.
        Change the original list.
    5. l.sort(key, reverse=False):
        Permantly changed the order of original list
        reverse=False ------> small to larger
        reverse=True  ------> large to small
        key: the sorting creteria ------> usually use "lambda"
    6. l.reverse():
        Permantly reverse the order of the original list
    7. l.pop(k=-1):
        Take out and return the element in k position.
        Default: the last element.
        The original list will change.
        Raises "IndexError" if list is empty or index is out of range.
    8. l.remove(x):
        Remove only the firt element x in l.
        If x is not found, raise "Value Error".
    8.1. del l[x]:
        Remove the element on position x
    8.2. del l:
        Remove the whole list objec
    9. l.index(x, [start, stop]):
        Return the position of the first element x.
        Raises "ValueError" if x is not found.
    10. l.count(x):
        Count the occurance of element x in list.
    11. l.copy():
        Return a copy of l.
        Use this if you don't want to change the original list.
    
"""
#1. clear
a = [1,2,3]
a.clear()

#2. append
[1,2,3].append(4)

#3. extend
a = [1,2,3]
a.extend(['a','b','c'])
a = [1,2,3]
a += ['a','b','c']

#4. insert
a = [1,2,3]
a.insert(0,'a')
a.insert(5,'b')

#5. sort
l = [5,4,1,2,3]
l.sort()
l.sort(reverse=True)

l1 = [['a', 4], ['c', 2], ['d', 1], ['b', 3]]
l1.sort(key=lambda x:x[0])
l1.sort(key=lambda x:x[0], reverse=True)
l1.sort(key=lambda x:x[1])
l1.sort(key=lambda x:x[0], reverse=False)

#6. reverse
l = [5,4,1,2,3]
l.reverse()

#7. pop
l = ['a','b', 'c','d']
x = l.pop()
x = l.pop(0)
x = l.pop(6) #----> IndexError

#8. remove
l = ['a', 'a', 'b', 'c', 'd']
l.remove('c')
l.remove('a')
l.remove('f') #----> ValueError

#8.1 del
del lis
del ['a','b','c', 'd', 'e'][2]
del ['a','b','c', 'd', 'e'][1:3]
del ['a','b','c', 'd', 'e'][1:4:2]

#9. index
l = ['a', 'b', 'b', 'c', 'd']
ind_a = l.index('a')
ind_b = l.index('b')
ind_x = l.index('x') #----> ValueError

#10. count
l = ['a', 'a', 'b', 'c', 'd']
count_a = l.count('a')
count_x = l.count('x') #-----> 0

#11. copy
l = [1,2,3]
l_1 = l
l_copy = l.copy()
l[1] = 'a'
print("Original: ", l)
print("Non copy: ", l_1)
print("Copy: ", l_copy)

#%% 4.1 Sequence Types: Tuple
"""
Immutable: Tuple ()
List is mutable but Tuple is not.
Most of the properties are the same,
    but only the process which will not change the content of the original sequence could be apply to Tuple.
"""
#e.g.
1,2,3
(1,2,3)
(1, 'a', 2, 'b', True)

#%% 4.2 Tuple: Getting Elements & Slicing
"""
    1. t[x]: 
        Return the object on position x.
        ~超出範圍會 raise error
    2. t[a:b:c]: 
        Return iterable(a copy) starting from position a, 
            ending at position b(excluded), and stepping c.
        The original iterable will not changed.
        ~超出範圍不error, 會return empty
"""
#1. get elements
('a','b','c')[0]
('a','b','c')[4]
('a','b','c')[-1]
('a','b','c')[-2]
a, b, c = ('a', 'b', 'c')
a, b, c = ('a', 'b', 'c', 'd', 'e')
a, b, *c = ('a', 'b', 'c', 'd', 'e')
a, *b, c = ('a', 'b', 'c', 'd', 'e')
*a, b, c = ('a', 'b', 'c', 'd', 'e')

#2. slice
('a','b','c', 'd', 'e')[1:3:2]
('a','b','c', 'd', 'e')[1:3:-1]
('a','b','c', 'd', 'e')[:3]
('a','b','c', 'd', 'e')[1:]
('a','b','c', 'd', 'e')[::-1]
('a','b','c', 'd', 'e')[:]

#%% 4.3 Tuple: Common Functions
"""
1. enumerate(t)
2. len(t):
    Count the number of elements in t.
3. min(t):
    Return the minimium value in t.
4. max(t):
    Return the maximium value in t.
5. sum(t):
    Return the summation of t.
6. zip([t1, t2, t3, ......])
7. sorted(iterable, key, reverse=False):
    Return a sorted list.
    The original list will not change.
    reverse=False ------> 由小到大
    reverse=True  ------> 由大到小
    key: the sorting creteria ------> usually use "lambda"
"""
#1. enumerate
for position, element in enumerate(('a', 'b', 'c', 'd')):
    print("The element in position {} is {}".format(position, element))

#2. len
len((1, 2, 3))

#3. min
min((1, 2, 3))

#4. max
max((1, 2, 3))

#5. sum
sum((1, 2, 3))

#6. zip
tuple(zip(('a','b','c'), (1,2,3), ('x','y','z')))

#7. sorted
t = (5,4,1,2,3)
t_sorted = sorted(t)
t_sorted_rev = sorted(t, reverse=True)

t1 = (('a', 4), ('c', 2), ('d', 1), ('b', 3))
t1_by_char = sorted(t1, key=lambda x:x[0])
t1_by_char_rev = sorted(t1, key=lambda x:x[0], reverse=True)
t1_by_numb = sorted(t1, key=lambda x:x[1])
t1_by_numb_rev = sorted(t1, key=lambda x:x[1], reverse=True)


#%% 4.4 Tuple: Common Methods
"""
Type help(tuple.*) in terminal to see the details of each method
    1. t.index(x, [start, stop]):
        Return the position of the first element x.
        Raises "ValueError" if x is not found.
    2. t.count(x):
        Count the occurance of element x in tuple.
"""
#1. index
t = ('a', 'b', 'b''c','d')
ind_a = t.index('a')
ind_b = t.index('b')
ind_x = t.index('x') #----> ValueError

#2. count
t = ('a', 'a', 'b', 'c', 'd')
count_a = t.count('a')
count_x = t.count('x') #-----> 0


#%% 5.1 Mapping Type: Dictionaty(dict)
"""
mutable, no order
combinations of several key-value pairs.
{key: value,
 key: value,
 key: value,
 ...........}

key can be any "immutable" type (int, float, tuple, string, boolean)
key must be unique

value can be any type
"""
a = {'three': 3, 'one': 1, 'two': 2}
b = dict({'three': 3, 'one': 1, 'two': 2})
c = dict(one=1, two=2, three=3)
d = dict({'one': 1, 'three': 3}, two=2)
e = dict([('two', 2), ('one', 1), ('three', 3)])
f = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

#%% 5.2 Dictionary: Getting and Setting items
"""
    1. dic[key]:
        Return the value of that key.
        Raise "KeyError" if key doesn't exist.
    2. dic[key] = value:
        Set key:value to dic.
        If key exists, change the value.
"""
a = {'three': 3, 'one': 1, 'two': 2}
a['three']
a['four']
a['four'] = 4
a['three'] = 6

#%% 5.3 Dictionary: Common Functions
"""
    1. len(dic):
        Number of items in dic
"""
a = {'three': 3, 'one': 1, 'two': 2}
len(a)


#%% 5.4 Dictionary: Common methods
"""
    1. dic.clear():
        Clear all items in the dic.
    2. dic.copy()
    3. dic.get(key[, x]):
        Return the value of the key.
        If key doesn't exist, return x.
    4. dic.keys():
        return only the keys.
    5. dic.values():
        Return only the values.
    6. dic.items():
        Return all the items, i.e. key:value, in the dic.
    7. dic_1.update(dic_2):
        Update dic_1 with dic_2.
        If key is overlaped, use the value in dic_2.
    8. dic.fromkeys(lis, val):
        Construct a new dic using the lis as keys, and initiate all value with val.
    9. dic.setdefault(key, value):
        If key is in dic, return the value of that key from the dic, and don't change the dic.
        If key is not in dic, set a new key:value pair to the dic.
    10. dic.pop(key):
        Return the value of the key, and remove the key:value from the dic.
        Raise "keyError" if key doesn't exist in dic.
    11. dic.popitem():
        Return and remove one key:value randomly from the dic.
        Raise "keyError" if key doesn't exist in dic.
"""
#1. clear
a = {'three': 3, 'one': 1, 'two': 2}
a.clear()

#2. copy
a = {'three': 3, 'one': 1, 'two': 2}
b = a.copy()
a['three'] = 4

#3. get
a = {'three': 3, 'one': 1, 'two': 2}
a.get('three')
a.get('four')

#4. keys
a = {'three': 3, 'one': 1, 'two': 2}
a.keys()

#5. values
a = {'three': 3, 'one': 1, 'two': 2}
a.values()

#6. items
a = {'three': 3, 'one': 1, 'two': 2}
a.items()

#7. update
a = {'three': 3, 'one': 1, 'two': 2}
a.update({'four': 4, 'five': 5, 'one':-1})

#8. fromkeys
a = {}.fromkeys(['a', 'b', 'c', 'd'], 6)

#9. setdefault
a = {'three': 3, 'one': 1, 'two': 2}
a.setdefault('four', 4)
a.setdefault('one', -1)

#10. pop
a = {'three': 3, 'one': 1, 'two': 2}
a.pop('one')
a.pop('four')

#11. popitems
a = {'three': 3, 'one': 1, 'two': 2}
a.popitem()

#%% 6.1 Set Type: Set
"""
{}
Every item in set is unique.
Dictionary without values.
items could be immutable type: int, float, string, tuple
"""
{1,2,3}

#%% 6.2 Set: Operation
"""
    1. Intersection:
        &
    2. Union:
        |
    3. Difference:
        -
    4. Symmetric Difference:
        ^
    5. ==
    6. !=
    7. in 
    8. not in
"""
#%% 6.3 Set: Common Functions
"""
    1. len(s):
        Returns an int type specifying number of elements in s.
"""
a = {1,2,3,4,5}
len(a)

#%% 6.4 Set: Common Methods
"""
    1. s.add(x)
    2. s.clear()
    3. s.copy()
    4. s1.isdisjoint(s2):
        If s1 and s2 have intersection, return False.
    5. s1.issubset(s2):
        If s1 is subset of s2, return True.
    6. s1.issupperset(s2):
        If s1 is supperset of s2, return True.
    7. s.pop():
        Randomly remove and return one item in s.
    8. s.remove(x):
        Delete x from s.
        If x not exist, raise "KeyError".
    9. s.discard(x):
        delete x from s.
        If x not in s, do nothing no error.
    10. s1.difference_update(s2):
        Update s1 with the s1-s2.
    11. s1.intersection_update(s2):
        Update s1 with the intersection of s1 and s2.
    12. s1.symmetric_differende_update(s2):
        Update s1 with the symmetric difference of s1 and s2.
    13. s1.update(s2):
        Update s1 with the union of s1 and s2.
"""
#1. add
s = {1, 2, 3, 4}
s.add('a')

#2. clear
s = {1, 2, 3, 4}
s.clear()

#3. copy
s = {1, 2, 3, 4}
s_copy = s.copy()
s.add(5)

#4. isdisjoint
s1 = {1,2,3}
s2 = {2,3,4}
s3 = {4,5,6}
s1.isdisjoint(s2)
s1.isdisjoint(s3)

#5. issubset
s1 = {2,3}
s2 = {1,2,3}
s3 = {2}
s1.issubset(s2)
s1.issubset(s3)

#6. issupperset
s1 = {2,3}
s2 = {1,2,3}
s3 = {2}
s1.issuperset(s2)
s1.issuperset(s3)

#7. pop
s = {1, 2, 3, 4}
s.pop()

#8. remove
s = {1, 2, 3, 4}
s.remove(1)
s.remove(5) #----> error

#9. discard
s = {1, 2, 3, 4}
s.discard(1)
s.discard(5) #----> nothing

#10. difference_update
s1 = {1,2,3}
s2 = {1,2}
s1.difference_update(s2)

#11. intersection_update
s1 = {1,2,3}
s2 = {1,2}
s1.intersection_update(s2)

#12. symmetric_differende_update
s1 = {1,2,3}
s2 = {1,2,4,5}
s1.symmetric_difference_update(s2)

#13. update
s1 = {1,2,3}
s2 = {1,2,4,5}
s1.update(s2)

#%% 7.1 Boolean(True / False)
"""
Two Types: True, False
In most case, it is used to control process.
"""
int(True) #----> 1
int(False) #----> 0
float(True) #----> 1.0
float(False) #----> 0.0

"""
Default False type:
    0
    0.0
    ''
    []
    ()
    {}: empty dictionary
    {}: empty set
"""

    

#%% 7.2 Boolean Operator
"""
    x or y (x | y)
    x and y (x & y)
    not x
"""

#%% 8.1 Type Transformation: int() & float(), str(), list(), tuple(), dict(), set()
"""
int v.s. float
"""
int(1.5)
int(1.0)
float(1)
float(1.5)

"""
int & float v.s. str
"""
int('apple') #----> error
float('apple') #----> error
int('1')
float('1')
int('1.5') #----> error
float('1.5')

"""
str v.s. list
"""
list('apple')
str(['a','b','c'])

"""
list v.s. set
"""
set([1,1,2,2,3,3,4,4,5])

#%% Appendix A: Statistic pachage
"""
The document link:
    https://docs.python.org/3/library/statistics.html
"""
import statistics
lis = [1,2,2,2,3,4,5,5,6,7,8,9,10]
ari_mean = statistics.mean(lis)
geo_mean = statistics.geometric_mean(lis)
har_mean = statistics.harmonic_mean(lis)
median = statistics.median(lis)
mode = statistics.mode(lis)
quantile_each = statistics.quantiles(lis)
stdev_pop = statistics.pstdev(lis)
stdev_sam = statistics.stdev(lis)
var_pop = statistics.pvariance(lis)
var_sam = statistics.variance(lis)

x = [1,2,3,4,5,6]
y = [-1,10,5,6,2,-9]
cov_xy = statistics.covariance(x,y)
corr_xy = statistics.correlation(x,y)
slope, intercept = statistics.linear_regression(x,y)



