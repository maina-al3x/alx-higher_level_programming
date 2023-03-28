#!/usr/bin/python3
"""
Printing a square
"""


class Square:
    """define variables and methods"""
    def __init__(self, size=0):
        """initialize attributes"""
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """define area method, evaluate square area"""
        return self.__size ** 2

    def my_print(self):
        """define my_print method, printing of a square"""
        if self.__size is 0:
            print('')
        for j in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print('')
