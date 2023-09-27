#!/usr/bin/python3
"""" A module to work with Nodes and Method of a Singly_Linked list"""


class Node:
    """ A class that defines the structure of singly-linked list """

    def __init__(self, data, next_node=None) -> None:
        """ Construct a new node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ A getter method for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """ A setter method for data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ A getter method for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ A setter method for next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class that represent a SinglyLinkedList """

    def __init__(self) -> None:
        """ Construct a SinglyLinkedList object"""
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new Node into the correct sorted position in the list
          (increasing order)
          """
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
        else:
            temp = self.__head

            if temp.data > new_node.data:
                new_node.next_node = self.__head
                self.__head = new_node
                return

            while (temp and temp.data < new_node.data):
                prev = temp
                temp = temp.next_node

            prev.next_node = new_node
            new_node.next_node = temp

    def __str__(self) -> str:
        """ Returns a string representation of the SinglyLinkedList. """
        temp = self.__head

        if not temp:
            return ""
        l_nodes = []
        while (temp):
            l_nodes.append(str(temp.data))
            if temp.next_node is not None:
                l_nodes.append("\n")
            temp = temp.next_node
        return "".join(l_nodes)
