"""
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    
    greeting = func("eda")
    print(greeting)
    
greet(shout)

def create_adder(x):#decorator function
    def adder(y): # anonmyoys function
        return x + y
    
    return adder

add = create_adder(15)
print(add(10))
"""
""" in web
def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2*x
    return inner

@decor1
@decor2

def num():
    return 2

@decor2
@decor1
def num2():
    return 2
print(num())
print(num2())
"""

"""Task1
1. A decorator that repeats a function call a specified number of times
"""
    

def decorator(func):
    def inner():
        for i in range(3):
            func()
    return inner


@decorator
def my_function():
    print("Hello, world!")
    
my_function()

"""
Create a decorator my_logger that logs the name of the function being called 
and the arguments it was called with. The logger should output the function name 
and arguments to the console each time the function is called.
"""
"""
def decorator(): # there is no decorator
    def inner(*args, **kwargs):
            print(f"args {args} and kwargs {kwargs}")
    return inner
x = decorator()
x(2, 3)
"""
def decorator(func):
    def inner(*args, **kwargs):
            print(f" args {args} and kwargs {kwargs}")
            return func(*args,**kwargs)
    return inner

@decorator
def my_function(a, b):
    print(a,b)
    
my_function(2, 3)
"""

import json

a = {"name":"eda","age":24}
print(type(str(a)))
b = json.dumps(a)
dictt  = json.loads(b)
print(type(dictt))
#serialization
var = {
       "Subjects":{
           "Maths":85,
           "Physic":90
           }
       }

with open("sample.json","w") as p:
    json.dump(var,p)
    
with open("sample.json","r") as f:
    json.load(f)
    
"""
"""
Find the average value of a specific key in a JSON file containing an array of dictionaries:
Write a Python program that reads a JSON file containing an array of dictionaries, 
calculates the average value of a specific key across all dictionaries in the array, 
and prints the result. For example, given the following JSON file named data.json
"""

import json

with open('data.json') as f:
    temp = json.load(f)

tot = 0
count = 0
for t in temp:
    if 'score' in t:
        tot += t['score']
        count += 1

avg = tot / count
print(avg)

"""
Write a Python program that reads a JSON file containing a list of numbers, finds the maximum and minimum values, and prints them to the console.
"""
with open('number.json') as f2:
    temp2 = json.load(f2)
    
print("max",max(temp2))
print("min",min(temp2))


