#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1.py import add, sub, mul, div

    def add(a,b):
        a = 10
        b = 5

        return (a + b)
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


    def sub(a,b):
        a = 10
        b = 5

        return (a - b)
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))


    def mul(a,b):
        a = 10
        b = 5
       
        return (a * b)

    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))


    def div(a,b):
        a = 10
        b = 5

        return int(a / b)
    
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

