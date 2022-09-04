# -*- coding: utf-8 -*-
#%% Class
"""
    1. Define a new categrary of type, i.e. Class,
        and use it to create objects belonging to it, i.e. Instances.
    2. Every object in Python has its own attributes and methods.
    3. Class and Instances are all objects in Python.
"""


#%% Attributes
"""
Variables of a object(could be a class or an instance) which charactize that object.

Attribute types:
    1. Class Attributes:
        Variables of a class that are shared between all of its instances and owned by the class itself.
        How to call:
            Class_Name.Attribute_Name
            
    2. Instance Attributes:
        Variables of a instance that are owned by the instance itself.
        How to call:
            Instance_Name.Attribute_Name
            
    3. Private Attributes:
        A private attribute cannot be accessed or changed directly.
        Class or instance attributes can all be either private or non-private attributes.
        How:
           Class_Name.__Attribute_Name
           Instance_Name.__Attribute_Name
"""

#%% Methods
"""
Functions of a specific object(could be a class or an instance).

Methods types:
    1. Class Methods:
        Functions belonging to the class itself.
        Start with:
            @classmethod
        How to call:
            Class_Name.Method_Name()
    
    2. Instance Methods:
        Functions belonging to the instance not the class.
        How to call:
            Instance_Name.Method_Name()
     
    3. Static Methods:
        Functions that are not associated with neither the class nor its instances.
        Do not need a class or a instance as an input.
        Start with:
            @staticmethod
        How to call:
            Class_Name.Method_Name()
            
    4. Private Methods:
        A private method cannot be accessed directly.
        Class or instance methods can all be neither private or non-private methods.
        
        How:
            __Method_Name()

    4. Special Methods:
        a. __str__():
            Use to set what you want to present when printing the object.
            How to call:
                print(Class_Name) or print(Instance_Name)
        
        b. __repr__():
            Use to set what you want to present when directly call the object in the terminal.
            How to call:
                Class_Name or Instance_Name
        
        c. __len__():
            Use to set what you want to present when using the 'len' function on the object.
            How to call:
                len(Class_Name) or len(Instance_Name)
        
        d. __iter__():
            Use to define how to iterate the object.
            How to call:
                for i in Class_Name:
                    .......
                for i in Instance_Name:
                    .......
                    
        e. Comparison Methods:
            Define how to compare (>,>=,<,<=,==,!=) two objects.
            I. __eq__():
                obj_1 == obj_2
            II. __ne__():
                obj_1 != obj_2
            III. __lt__():
                obj_1 < obj_2
            IV. __gt__():
                obj_1 > obj_2
            V. __le__():
                obj_1 <= obj_2
            VI. __ge__():
                obj_1 >= obj_2
        
        f. Arithmetic Methods:
            Define how to do arithmetic calculation (>,>=,<,<=,==,!=) on two objects.
            I. __add__():
                obj_1 + obj_2
            II. __sub__():
                obj_1 - obj_2
            III. __mul__():
                obj_1 * obj_2
            IV. __floordiv__():
                obj_1 // obj_2
            V. __truediv__():
                obj_1 / obj_2
            VI. __mod__():
                obj_1 % obj_2
            VII. __pow__():
                obj_1 ** obj_2
            
"""

#%% Inheritance
"""
When one class is almost fitted our need but we need to change a little bit on it, 
    for instance, to add new methods or attributes, or to modify the original class.
The class that is inheritated from other classes is called a "child class", or a "derived class".
The class that another class is inheritated from is called a "parent class", a "base class", or a "superclass".
The child class has all the attributes and the methods of its parents class.
"""

#%% Example: Bank
class Bank():
    numb_account = 0  # class attributes
    __total_balance = 0
    name = "Normal"
    def __init__(self, name, balance, ID):  # initiation 
        #print("In Bank __init__")
        self.__name = name
        self.__balance = balance
        self.account_id = ID
        self.__class__.numb_account += 1
        self.__class__.__total_balance += balance
        
    def save_money(self, money_save):
        self.__balance += money_save
        self.__class__.__total_balance += money_save
        print("Saved {} dollars".format(money_save))
    
    def withdraw_money(self, money_wit):
        self.__balance -= money_wit
        self.__class__.__total_balance -= money_wit
        print("Withdrawed {} dollars".format(money_wit))
    
    def get_balance(self):
        print("Account {}'s current balance: {}".format(self.__name, self.__balance))
        return self.__balance
    
    @classmethod
    def get_total_balance(cls):
        print("Current total balance: {}".format(cls.__total_balance))
        return cls.__total_balance
    
    @classmethod
    def show_bank_info(cls):
        print("Current total balance: {} \nCurren total numbers of account: {}".format(cls.__total_balance, cls.numb_account))
   
    @staticmethod
    def print_xx():
        print("I am a Bank")


class BOA(Bank):
    level_rate = {1: 1.001,
                  2: 1.002,
                  3: 1.003,
                  4: 1.004,
                  5: 1.005}
    numb_account = 0
    __total_balance = 0
    name = "BOA"
    def __init__(self, name, balance, ID, cust_level):  # initiation 
        #print("In BOA __init__")    
        self.__cust_level = cust_level
        self.__cust_rate = self.__level_to_rate()
        super().__init__(name, balance, ID)
    def __level_to_rate(self):
        rate = BOA.level_rate[self.__cust_level]
        return rate
    def save_money(self, money_save):
        money_save = money_save * self.__cust_rate
        self._Bank__balance += money_save
        self.__class__.__total_balance += money_save
        print("Saved {} dollars".format(money_save))


# class CHASE(Bank):
#     numb_account = 0
#     __total_balance = 0
#     name = "CHASE"
#     app_rate = 1.003
#     web_rate = 1.002
#     def __init__(self, name, balance, ID):
#         self.__balance = balance
#         self.__name = name
#         self.id = ID
#         print("In CHASE __init__")
#     def save_money_app(self, money_save):
#         money_save *= CHASE.app_rate
#         self.__balance += money_save
#         CHASE.__total_balance += money_save
#         print("Saved {} dollars through app.".format(money_save))
#     def save_money_web(self, money_save):
#         money_save *= CHASE.web_rate
#         self.__balance += money_save
#         CHASE.__total_balance += money_save
#         print("Saved {} dollars through web.".format(money_save))
        
        
class CHASE(Bank):
    numb_account = 0
    __total_balance = 0
    name = "CHASE"
    app_rate = 1.003
    web_rate = 1.002
    def __init__(self, name, balance, ID):
        #print("In CHASE __init__")
        super().__init__(name, balance, ID)
    def save_money_app(self, money_save):
        money_save *= CHASE.app_rate
        self._Bank__balance += money_save
        self.__class__.__total_balance += money_save
        print("Saved {} dollars through app.".format(money_save))
    def save_money_web(self, money_save):
        money_save *= CHASE.web_rate
        self._Bank__balance += money_save
        self.__class__.__total_balance += money_save
        print("Saved {} dollars through web.".format(money_save))
        

class MyBank(BOA, CHASE):
    numb_account = 0
    __total_balance = 0 


Account_1 = MyBank('A',1000,1, 4)
Account_2 = MyBank('B',2000,2, 3)
Account_1.save_money_web(200)
Account_1.save_money_app(100)
Account_1.save_money(100)

Account_1.get_balance()