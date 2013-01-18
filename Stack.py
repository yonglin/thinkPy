# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 10:43:49 2013

@author: yuege
"""

class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)
    
    def printList(node):
        while node:
            print node,
            node = node.next
        print
    
    def removeSecond(list):
        if list == None:
            return
        first = list
        second = list.next
        # make the first node refer to the third
        first.next = second.next
        # separate the second node from the rest of the list
        second.next = None
        return second
        
    def printBackward(self):
        if self.next != None:
            tail = self.next
            tail.printBackward()
        print self.cargo
        
class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        
    def printBackward(self):
        print "[",
        if self.head != None:
            self.head.printBackward()
        print "]",
    
    def addFirst(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length +1
            
    
    
#def printBackward(list):
#    if list == None:
#        return
#    head = list
#    tail = list.next
#    printBackward(tail)
#    print head,
#
#def printBackwardNicely(list):
#    print "[",
#    printBackward(list)
#    print "]",
    

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        return (self.items == [])

def evalPostfix(expr):
    import re
    tokenList = re.split("([^0-9])", expr)
    stack = Stack()
    for token in tokenList:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        
    def isEmpty(self):
        return (self.length == 0)
        
    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # is list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next:
                last = last.next
                # append the new node
            self.length = self.length + 1
    
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo
        
class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
    def isEmpty(self):
        return (self.length == 0)

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = Node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length = self.length + 1
    
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:
            self.last = None
        return cargo
          
class QueueADT:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return (self.items == [])
    
    def insert(self, item):
        self.items.append(item)
    
    def remove(self):
        tmp = self.items[0]
        del self.items[0]
        return tmp
class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def insert(self, item):
        self.items.append(item)
    
    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        self.items[maxi : maxi+1] = []# 删除list中知道索引的某一元素的小技巧
        return item
        
class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)
    
    def __cmp__(self, other):
        if self.score < other.socre:
            return 1
        if self.score > other.score:
            return 1
        return 0
            
        
        
        
        
        
        