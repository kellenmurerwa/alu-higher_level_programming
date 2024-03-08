#!/usr/bin/python3
"""define class square"""


class Square:
    """define empty class square"""

    def __init__(self, size=0):
        """define __init__ method"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """define set size method"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """define area method"""
        return self.__size ** 2
