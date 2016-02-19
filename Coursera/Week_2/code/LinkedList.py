#!/usr/bin/python3

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, first=None):
        self.first = first

    def is_empty(self):
        return self.first == None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.first
        self.first = new_node

    def pop(self):
        data = self.first.data
        self.first = self.first.next_node
        return data
