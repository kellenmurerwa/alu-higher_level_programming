#!/usr/bin/python3
from calculator_1.py import add, sub, mul, div

a = 10
b = 5
def add(a,b):

    return (a + b)


def sub(a,b):

    return (a - b)


def mul(a,b):
       
    return (a * b)


def div(a,b):

    return int(a / b)
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
