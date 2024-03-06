#!/usr/bin/python3
"""
A script that defines a Node class singly linked list
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
    __data: The data stored in the node.
    __next_node: Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node with the given data and next node reference.

        Params:
        data: The data to be stored in the node
        next_node: The next node in the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data stored in the node.

        Returns:
        The data in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data stored in the node.

        Params:
        value: The new value for the data.

        Raises:
        TypeError: If the value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node.

        Returns:
        Reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the reference to the next node.

        Params:
        value: The reference to the next node.

        Raises:
        TypeError: If the value is not a Node object.
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
    __head: The head node of the list.
    """

    def __init__(self):
        """
        Initializes an empty SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        if not result:
            return ""
        return result[:-1]

    def sorted_insert(self, value):
        """
        Inserts a new node in the correct position in the list

        Params:
        value: The value to be inserted in the list
        """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
