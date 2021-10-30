# Python has reserved words which we cannot re use in our program, they have predefined meaning
# Ex: False, class, return, is, finally, None, if, for, lambda etc.
# Interactive : Running line by line
# Script : Running by writing in the file
# Program steps or Programming Flow
# Conditional, Sequence, Repeated
# Conditional 
# a = 5
# if(a==5): 
#     print("tulasidas")
# else:
#     print("dikku")

# Variables, Expresssions, and Statements
# Constants: Fixed values whose values cannot be changed, such as numbers, letters, and Strings.
# String Constants use single and doble quotes
# print(4.5)
# print(5)
# print("tulasidas")
# Variable : A variable is a named place in the memory where programmer can store data and retrieve the data by using the data name
# Programmer can chose the  name of the variable
# Programmer can change the value of the varible
# a = 5   #The value of a is integer type (Pyhton is dynamically typed language, that is we dont need to mention the datatype the interpreter itself understands the type of the data)
# print(a)
# a = "tulasidas"   #Here the value of a changed the interpreter itself changes the data type.
# print(a)

# Naming convention for variables in python code
# 1.Must start with a letter or underscore
# 2.Must consist of letters and numbers
# Case sensitive
# We can also use descriptive names for variables it is upto the programmers choice whether to chose descriptive name or not.

# Expressions 
# Operator                  Operation
#   +                    Addition
#   -                    Substraction
#   *                    Multiplication
#   /                    Division
#  **                    Power
#   %                    Remainder 


# Order of Evaluation
# Paranthesis are always respected
# Exponentiation (Raise to power)
# Multiplication, Division, and Remainder
# Addiiton, Substraction
# Left to Right

# Type in Python
# In python variables, literals, and constants have types
# Python knows the differnece between Strings and Integer types
# For example '+' means  additon if something is number, if something is a string then it is called concatination
# d = 1 + 2   #Addition of two numbers
# print(d)  
# str = "Tulasidas "+"Biradar"    #Concatination of two strings
# print(str)   

# Type Matters 
# Python knows what type of everything
# Some operartions are prohibited
# You cannot add 1 to a string
# a = 3
# str = "tulasidas"+a              #TypeError: can only concatenate str (not "int") to str

# Type conversions
# When you put an integer and a floationg point in an expression, the integer implicitly converted into float
# You can control this by using the implicit functions int(), float()
# print(float(9)+9)    #answer is 18.0
# a = 6
# f = float(a)
# print(f)  #6.0
# Integer division produces floating value
# print(5/2);
# String Coversion
# we can use int() and float() to convert between Strings and Integers
# You will get an error if you try to convert a string which is does not contain numbers
# val  = '123'
# a = int(val)
# print(a)
# str = 'abc'
# a = int(str)
# print(a)     #ValueError: invalid literal for int() with base 10: 'abc'

# User Input 
# We can instruct python to pause and read the data from the user by using input() function
# The input() function returns a string
# a = input("Enter the value")
# print(type(a))   #<class 'str'>

# name = input("Eter your name ")
# print("Welocome "+name)

# Comments in Python
# Anything that comes afer # is called as comment
# What is a Comment?
# Desribes what is going to happen in the code
# Turn off a line of code perhaps temporirily

# Boolean Expressions
# Asks a question and returns True or False
# Comparision opearator looks at the variables but do not change the value of the variable

# Python                  Meaning
# <                     Less than
# <=                    Less than or equals
# ==                   Equal
# >                         Greate than
# >=                     Greate than equals
# !=                          not equlals


# Python is an indented language so you need to maintain intendation
# Conditional execution: if statement
# x = 5
# if(x>1):
#     print(x)   #Here we need to maintain indentaition                 

# Conditional execution else statement
# a = 5
# if(a>1):
#     print("the number is greater than 1")
# else:
#     print("the number is less than 1")

# try and except stucture 
# You should surround a dangerous section of the code with try and except
# If the code in the try runs properly then except code is skipped
# If the code in the try fails then it jumps to except block


# a = "tulasidas"
# try:
#     b = int(a)
# except:
#     print("Error Occured")
# Def keyword is used for defining functions
# def add():    #Here def is a keyword and add is a function name
#     a = 5
#     b = 6
#     print(a+b)
# add()            #Here we are calling the funtion

# There are two types of funtions in python built in and user defined 
# Built in functions have predefined funcionality in them where as we can define the functionality of the userdefined funtion
# Built in function example: print(), input(), type(), int(), flot()
# In python a fuction is some reusable code that takes some input, does some computation and return a value
# We define the function by using the reserved keyword def
# We call the function by using the function name and using the paranthesis and passing arguments inside the paranthesis
# def add(a,b):
#     return a+b               # Retuns the additon of two values
# print(add(5,4))              # We need to print the return value so we use print

# String conversion 
# You can convert a stirng to an integer or float, if the string contains numbers
# a = '123'
# print(type(a))     #<class 'str'>
# b = int(a)         #<class 'int'>
# print(type(b))

# Functions of our own 
# In order to create user defined function we use def keyword, and indent the body of the function
# This is called definition of funtion, the function gets executed only when we call it 
# When we defined a function we can call it and use it as many times as we want 
# This is store and reuse pattern
# Argument: An argument is a value we pass into the function as its input when we call the function
# Parameters : A parameter is a variable which we use in the function definition

# def addition(a,b):                #Here a and b are called as parameters
#     return a+b                    #Returns a value
# val = addition(5,4)               #Here a and b are called as arguments
# print(val)

# We have to match the number of parameters and number of arguments
# When a function does not returns anyhting we call it void function

# Loops and Iteration
# Loops (Reapted steps)  have iteration variable that change each time throug a loop. Often these iteration variables go through a sequence of numbers
# The loop get executed until the specified condition is wrong or False

# Breaking out of the loop
# The break statement is used to jump out of the loop and execute the statements followed by the loop
# while(True):
#     line = input('>')
#     if(line == "done"):
#         print("The loop exection is completed")
#         break                                                #break statement helps to break out of the loop

# Finishing an iteration with continue statement
# while True:
#     line = input(">")
#     if line[0] == "#":
#         continue
#     if line == "done":
#         break
#     print(line)

# Indefintite loops 
# While loops are indefinite loop because they keep on going until a logical condtion becomes false
# while True:
#     a = input(">")
#     if(a==1):
#         break

# Definite Loops 
# The loops which execute for exact amount of time are called definite loops
# We can say that definite loops iterate through the member of a set

# for i in [1,2,3,4]:
#     print(i)

# A definite loop with strings

# for friend in ["tulasi",'dillu',"dikku"]:    #The loop iterates through each string in the list
#     print(friend)
# Definite loop(For loop): Definite loops have explicit iteration variables that change each time through a loop. These iteration variable move through sequence or set

# Finding the largest number using the loop
# list = [1,2,3,4,5]
# max = list[0]
# for i in list:
#     if max<i:
#         max = i
# print(max)

# Counting number of elements using Loops
# list = [1,2,3,4]
# count = 0
# for i in list:
#     count+=1
# print(count)    #Retruns 4 because the number of elements in the list are four

# a = None             #Here None means emptyness
# print(a)
# We can use 'is' and is not as operators in python
# is opearator implies same as
# is operator is stronger than == operator

# Strings in Python
# A String is a sequence of characters
# A String literal uses single quotes or double quotes
# For strings + means concatination

# Reading and converting strings
# We prefer to read the data in the string format, and then parse and convert into the data we want

# Looking inside the string
# we can get any single character in string by using the specified index in square brackets
# a = "tulasidas"
# print(a[0])   #Returns the value at 0th index
# A character too far in the string
# If you try index beyond the end of the string you will get an error

# str = "tulasi"
# print(str[10])    #IndexError: string index out of range

# Strings have length, the built in function in len in python gives the length of the function

# str = "tulsidas"
# print(len(str))   #8

# here above len is a predifined function which takes a string as an input and returns the length as output
# Looping through strings 
# index = 0
# name = "tulasidas"
# while index<len(name): #loop iterates until the lenggth of the string
#     print(name[index])  #Prints element at each index
#     index += 1     #Index value is increased by one

# name = "tulasidas"
# for letter in name:       #Here letter is an iterator varible which iterates through each character in the string
#     print(letter)         #Here letter is an individual character in the string and name is the entire string

#More string operations
# We can also look at any continuous string in the given main string by using colon operator
# name = "tulasidas"
# print(name[:])   #we have to mention the first index and the second index, if we dont mention first index then it wil take from 0th index and if we dont mention the second index it will go upto the length of the string

# String Concatination Operation
# name = "tulsidas " 
# surname = "biradar"  
# print(name + surname)           # when we use + operator for strings it will concatinate both the strings

# The 'in' keyword is used to check whether something is there in the string or not

# fruit = "banana"
# print('n' in fruit)      # return True because n is in the string

# We can also compare strings 
# fruit1 = 'Apple'
# fruit2 = 'Banana'
# fruit3 = "banana"
# print(fruit1>fruit2)      #Return false because B is greater than A
# print(fruit1<fruit3)      #Returns True because b is greater than A

# Python has a string library which has number of predefined functions, we can use these predefined function to perform operations on strings

# The function do not modify the strings, instead they create new Strings
# name = "TULASIDAS"
# print(name.lower())     #Converts the entire string into lower case


# We can find whether a sunstring present in the main string or not by using find()
# Find return the index of first occurance of substring in the given main string
# If the substring is not in the main string then it will return -1

# name = "tulasidas biradar wasar"
# print(name.find("tu"))   #0            # Here we have to pass the substring that we want to find out in the find() function
# print(name.find("Z"))    #-1


# Search and Replace operations on string
# The replace method is used to find the string and replace it with new string
# name = "tulasidas biradar wasar"
# print(name.replace("tulasidas","Gnaneshwar"))      #Find the string tulasidas and replaces with new string gnaneshwar
# print(name)      #Strings are immutable in Python

# We can remove the white spaces from the string in the beginning or in the end by using strip
# lsstrip() is used to strip the white spaces from the beginning of the string
# rsstrip() is used to strip the white spaces from the end of the string
# strip() is used to remove white spaces from the beginning and from the end of the string
# name = "      tulasdias          "
# str1 = name.lstrip()
# print(len(str1))    #19
# str2 = name.rstrip()
# print(len(str2))    #15
# str3 = name.strip()
# print(len(str3))   #9


# We can aslo check whether a string starts with a particular substr or not by using startswith("substr")
# It returns true or false value
# name = "tulasidas biradar"
# print(name.startswith("tulasidas"))   # Returns True because name starts with tulasidas
# print(name.startswith("man"))         # Returns False because name doesnt starts with man


#Parsing and extracting data from the string
# name = "name: tulasidas surname:biradar @gmail:dasbiradar1999@gmail.com_"
# spos = name.find("@")
# print(spos)
# epos = name.find("_",spos)
# print(epos)
# print(name[spos+1:epos])               #here epos is exclusive, spos is inclusive

# Reading Files 
# File proceesing

# A Text file can be taught of as a sequence of lines
# Before we can read the contents of the file, we must tell python which file we are going to work with and what will be doing with the file
# This is done with the open() 
# open() returns a file handle a variable used to perform operations on the file

# fhandle = open("tulasi.txt","r")    # The first argument is file name and second argument is mode of operation( read, write etc), mode of operation is optional
# For reading we use "r" as mode of operation, for writing we use "w" as mode of operation

# fhandle is not a file, or data in the file, fhandle is just a text wrapper
# If the file is not existing then it returns no such file or directory : gives the file name


# The new line Character
# \n is used to indicate next line
# \n is just one character
# stuff = "x\ny"
# print(stuff) 
# print(len(stuff))   # Return 3 because the length of the string is 3

# Working with Files in python
# fhandle = open("file.txt")
# for line in fhandle: 
#     line = line.rstrip()                       # Here line represents each line in the file, here we use rstrip to remove the white spaces at the end of each line
#     print(line)

#Counting number of lines in the file
# fhandle = open("file.txt")
# count = 0
# for line in fhandle:
#     count += 1
# print(count)     # returns 7 since the number of lines in the file are 7

# Reading the whole file into a single string
# fhandle = open("file.txt")    # Opening the file file.txt
# str = fhandle.read()          # Reading  the entire file into a single string
# print(len(str)) 
# print(str[:20])    #prints first 20 characters in the string str 
# We can strip the white spaces from the right hand side of the string using rstrip() from string library
# The new line is also considered as white space and is stripped
# We can use continue to skip the lines that we dont want to print
# We can also use 'in' keyword whether a particular string is in the line or not
# name = 'directory'
# fhandle = open("file.txt")
# count = 0
# for line in fhandle:
#     line = line.rstrip()
#     if name in line:
#         count += 1
# print(count)

# DataStructures in python
# Algorithm : A set of rules or steps used to solve a problem
# DataStructures: A particular way of organising the data in the compueter


# Most of the variables have one value in them, whenever we try to put a new value the old value gets overwritten
# name = "tulasidas"
# name = 5      # Here the value 5 overwrites the value tulasidas
# print(name)
# In order to over come the above problem we use collections
# In list we can store multiple values under a same variable name
# List can hold heterogenous elements
# lst = ["tulasdas",5,"dikku"]   # Here we are storing different types of values under same varible name lst
# print(lst[0]) 
# print(type(lst))   

# List constants are surrounded by square brackets and the elements in the list are seperated by commas
# A list element can be any python object even another list
# Looping through lists
# lst = ['tulasidas',"biradar","wasar"]
# for item in lst:
#     print(item)

# Looking Inside the Lists
# Just like strings we can get any single element in a list using an index specified in square brackets
# friends = ["tulsidas","biradar","wasar"]
# print(friends[0])

# Strings are immutable: we cannot change the contents of the string
# Lists are mutable : we can change the contents of the List
# fruit  ="Banana"
# # fruit[0] = "t"
# # print(fruit)  #TypeError: 'str' object does not support item assignment
# x = fruit.lower()   # Here the string is not changed but a new string x is created and in that we are storing the value
# print(x)

# lst = [1,2,3,4,5,6,67]
# lst[0] = 3   # Here no new lists are created but the existing value in the list is changecd
# print(lst)  # Lists are mutable, we have changed the value of lst[0]
# We can find out the length of the function list by using the len() function
# lst = [1,2,3,4,5,6]
# print(len(lst))    # len() function returns the length of the function i,e how many elements are there in the list

#  The Range function 
#  The range function returns a list of numbers that range from zero to one less than a the parameter
# Looping through list using the range function

# friends = ["tulasidas","dikku","gnanu"]
# for i in range(len(friends)):              # i is an integer iterator
#     print(friends[i])

# Lists Loop operation
# We can concatinate two lists by using + operator
# We can create a new list by adding two lists
# lst = [1,2,3]
# lst2 = [4,5,6]
# print(lst+lst2)    #[1, 2, 3, 4, 5, 6]

# Lists can be sliced using : operator
# t = [1,2,3,4,4,5]
# print(t[0:2])
# print(t)
# print(type(t))   #<class 'list'>

# Building the list from the scratch 
# We can add the element to the list by using append method
# The values in the list are stored in sequence and new elements are added at the end of the list

# stuff = list()
# stuff.append('Tulasi')   # Each element is added at the end of the list
# stuff.append("Dikku")
# stuff.append("Gnanu")
# print(stuff)   #['Tulasi', 'Dikku', 'Gnanu']

# To know whether something is in the list or not
# some = [1,2,3,4,5]
# print(1 in some)   # True, returns true because 1 is in the some

# Lists are in order
# Lists holds many values and keep those values in the order, until we something with the order 
# A list can be sorted by using the sort method
# lst = [7,6,5,1,2,3,9]
# lst.sort()              # Here the elements get sorted 
# print(lst)            # We are printing the sorted list



# Built in functions that takes list as arguments 
# lst = [1,2,3,4,5,6]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# str = "tulasidas biradar wasar"
# lst = str.split()    # Split function takes the delimeter as argument, if we dont pass any argument the default parameter would be white space
# print(lst)    #['tulasidas', 'biradar', 'wasar']

# fhandle = open("file.txt")   #opening the file 
# words = []          # Declaring an empty list 
# for line in fhandle:      
#     line = line.rstrip()
#     words = line.split()          #Converting the string into list by spitting into individuals items in a list
#     for word in words:
#         print(word)            #Printing individual words in the list


# List: A list is collection of values that stay in order
# Dictionary : A collection of values, each having its own label(Key)
# There is no sense of order in dictionary, everything has key value

# Dictionaries are pythons most powerful data collection  
# Dicionaries have key value pair, they don't have any order

# purse = dict()
# purse['makeup'] = "Fair and Lovely"
# purse['pens'] = 2
# print(purse['makeup'])
# print(purse['pens'])

# purse[3] = 5
# print(purse)
# print(purse[3])

# Dictionary literals use curly braces and have a list of key : value pairs 
# j = {1:"tulasidas",2:"biradar",3:'wasar'}
# print(j)
# print(j[1])
# print(j[2])
# print(j[3])

# Counting using dicionaries

# c = dict()
# c['cse'] = 1
# c['eee'] = 2
# print(c)
# c['eee'] = c['eee'] + 1   # 1 is added to the existing value of key value of eee and becomes  3
# print(c['eee'])


# If you try to print a key value which is not there in the dictinary then you will get error

# dic = {}
# print(dic['1'])   #KeyError: '1'
# print(1 in dic)

# Looping through dicionaries
# dict = {}
# names = ['cse','eee','civil','it','it','cse']
# for name in names:
#     if name not in dict:
#         dict[name] = 1
#     else:
#         dict[name] = dict[name]+1
# print(dict)
# print(dict.get("cse",0))    # To get the count of cse in the dictionaary initially the count value is zero

# dict={}
# names = ["cse","eee","it","ece","cse","eee"]

# for name in names:
#     dict[name] = dict.get(name,0) + 1   # dict.get(name, 0) returns the count of each key in the dicionary, the default value is zero 
# print(dict)

# fhandle = open('file.txt')
# dict = {}
# words = []
# for line in fhandle:
#     line = line.rstrip()
#     words = line.split(' ')
#     for word in words:
#         dict[word] =dict.get(word,0)+1
# print(words)
# print(dict)

# dict = {"tulasi":2,"dikku":4,"gnanu":5}
# for key in dict:
#     print(key,dict[key])

# print(dict.keys())    # Gives the keys in the dictIonary
# print(dict.values())  # Gives the values in the dicionary

#  Looping by using two variables in the dictionary

# dict = {"tulasi":2,"dikku":2}
# for key,value in dict.items():
#     print(key,value)

# Tuples : Tuples function much like list, lists are mutable where as tuples are immutable, once you have declared a list you cannot change the order of the list
# Tuples have elements indexed from 0
# Tuples uses paranthesis

# x = ('tulasi',1,'biradar')
# print(x[0])   # Here the value at the index 0 is tulasi

# y = (1,2,3,4,5,6)
# print(max(y))
# print(min(y))
# print(sum(y))
# tup = (1,2,3,4)
# tup[0] = 10      #TypeError: 'tuple' object does not support item assignment
# Tuples items do not support item assignment

# Tuples and assignment
# We can set tuples on the right side and assign values on the right side by using another tuple
# (tulasi,das,biradar) = (1,2,3)
# print(das)

# Dictionaries and tuples
# Dictionary method items() returns a list of [(key, value),(key, value),.......] tuples

# d = dict()
# d["tulasi"] = 1
# d["biradar"] = 2
# print(d.items())     # dict_items([('tulasi', 1), ('biradar', 2)])

# Tuples are comparable
# We can compare the tuples, if the first element is same in both the tuples then it will go to the next element.

# print((1,2,3,4,5)>(1,2,4,5,6))   # Returns false because 3 is lesser than 4

# We can sort the elements of the list
# Dictionary gives a list of tuples, when we use the method items
# We can comapre the elements in two different tuples
# By taking this as advantage we can sort the elements in the dictionary

# dict = {'a':1,'c':2,'b':3}
# print(sorted(dict.items()))    # [('a', 1), ('b', 3), ('c', 2)]
# for key,value in sorted(dict.items()):    #By default it will sort using the keys
#     print(key, value)


# We can also sort the dictionary elements by using the value

# dict = {'tulasi':9,'dikku':3,'biradar':3}
# lst = []  # Creating a list inorder to store tuples in the format of (value,key)
# for key, value in dict.items(): 
#     lst.append((value,key))                  # Adding tuples to the lst
# print(sorted(lst))

# Sets in Python

# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements
# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. 
# This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists.
# A set does not allows duplicate elements

# t = set([1,2,4,3,4])
# print(t)

# s = {1,2,3,4,5,6,7,7,7,7,77}   # We can define a set by using curly braces
# print(s)


# Object Oriented Programming in Python
# print(type("hello"))      # <class 'str'>

# Hello is an object of class str
# class Dog:
#     def bark(self):
#         print("Bark")

# d = Dog()    # Initialising an object or instance to he Dog class
# d.bark()     # Calling the function bark which is in the Dog class by using the instance/ object of the class Dog

# We have __init__ constructor which gets called when we inittialize an object to the class
# Constructor can be used to have initial/ default values for the variables
# class Dog:
#     def __init__(self,name,age):        # Constructor called when the object is created
#         self.name = name  
#         self.age = age
#     def show(self):
#         print(f" The name of the dog is {self.name}, the age of the dog is {self.age}")     # This printing is known as f string printing
# a = Dog("dikku",7)                # Passing the initial values, by using class name, which directly calls the constructor
# a.show()                             # Calling the show method

# Inheritence in Python
# class Dog:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name
#     def show(self):
#         print(f'I am {self.name}, my age is {self.age}')
#     def speak(self):
#         print("I didn't know what to speak")
# a = Dog(12,"tulasi")
# a.show()
# a.speak()

# Class attributes : The variables defined inside the class are called class attributes
# We can access the class attributes by using the class name
# class Dog:
#     number_of_people = 5                        # Attribute of the class 
#     def __init__(self,name):
#         self.name = name
        
# p1 = Dog("tim")
# print(Dog.number_of_people)                    # Printing the attribute value of the class
# Dog.number_of_people=6                         # Changing the attribute value of the class         
# print(Dog.number_of_people)

# Creating userdefined modules in python

# import arithmetic   # here we imported a module called arithmetic
# arithmetic.add(5,6)   # Calling the functions that are in the arithmetic module
# arithmetic.sub(9,6)
# arithmetic.mul(2,2)
# arithmetic.div(1,1)
# arithmetic.pow(2,4)


 








































