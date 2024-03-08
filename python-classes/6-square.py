#!/usr/bin/python3
"""define class square"""


class Square:
    """define empty class square"""

    def __init__(self, size=0, position=(0, 0)):
        """define __init__ method"""

        self.__size = size
        self.position = position

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

    def my_print(self):
        """define my_print method"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
            print(' ' * self.__position[0])

    @property
    def position(self):
        """define position method"""
        return self.__position

    @position.setter
    def position(self, value):
        """define pos meth"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
