#!/usr/bin/python3

class Node:
    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node

class LinkedList:
    def __init__(self, first=None):
        self.first = first

    def is_empty(self):
        return self.first == None

    def push(self, data):
        self.first = Node(data, self.first)

    def pop(self):
        if self.is_empty():
            return None
        else:
            data = self.first.item
            self.first = self.first.next_node
            return data
