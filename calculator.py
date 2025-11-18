#https://github.com/lemonadeDevsport/lab11-SD
#Sofia De Los Santos

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("a cannot be less than 0") # raise ValueError if a < 0
def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    else:
        return math.log(a,b)# use math library/raise ValueError

def exponent(a, b):
    return a**b
