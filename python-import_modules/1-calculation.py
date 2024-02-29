#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1.py import add, sub, mul, div

    a = 10
    b = 5
    def add(a,b):

        return (a + b)
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


    def sub(a,b):

        return (a - b)
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))


    def mul(a,b):
       
        return (a * b)

    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))


    def div(a,b):

        return int(a / b)
    
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
