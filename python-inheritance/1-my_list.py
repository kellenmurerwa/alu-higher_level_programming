#!/usr/bin/python3
"""First line of python"""


class MyList(list):
    """a child class inheriting from an inbuilt-class"""
    def print_sorted(self):
        """Writing a sorting function"""
        print(sorted(self))
