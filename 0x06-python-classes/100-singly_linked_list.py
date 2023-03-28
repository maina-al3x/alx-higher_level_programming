#!/usr/bin/python3
"""
Singly linked list
"""


class Node:
    """define variables and methods"""

    def __init__(self, data, next_node=None):
        """initialize attibute"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
#        print("Data stored: " + '{}'.format(self.__data))

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
#        print("Node created")


class SinglyLinkedList:
    """define variables and methods """

    def __init__(self):
        """initialize attibute"""
        self.__head = None

    def sorted_insert(self, value):
        """function that inserts a new_node"""
        new_node = Node(value, None)
        temp = self.__head
        if not self.__head:
            self.__head = new_node
#            print("hit 'if temp is None'")
#            print("New_node inserted")
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
#            print("hit 'temp.data > value'")
#            print("New_node inserted")
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
#        print("New_node inserted")
        return

    def __str__(self):
        """
        define special __str__ method for printing the list values
        when print(self) is called
        """
        list_values = ''
        temp = self.__head
        while temp is not None:
            list_values += str(temp.data)
            if temp.next_node is not None:
                list_values += '\n'
            temp = temp.next_node
        return list_values
