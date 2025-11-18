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
    except ValueError as e:
        raise ValueError("a cannot be less than 0") # raise ValueError if a < 0
def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <= 0 or a<= 0 or a ==1:
        raise ValueError("Log values are invalid")
    return math.log(b,a)# use math library/raise ValueError

def exp(a, b):
    return a**b
