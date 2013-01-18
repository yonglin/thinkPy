# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:37:14 2013

@author: yuege
"""

class Tree:
    def __init__(self, cargo, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.cargo)

def printTreePostorder(tree):
    if tree == None:
        return
    printTreePostorder(tree.left)
    printTreePostorder(tree.right)
    print tree.cargo,
    
def printTreeInorder(tree):
    if tree == None:
        return
    printTreeInorder(tree.left)
    print tree.cargo,
    printTreeInorder(tree.right)

def printTreeIndented(tree, level = 0):
    if tree == None:
        return
    printTreeIndented(tree.right, level+1)
    print ' '*level + str(tree.cargo)
    printTreeIndented(tree.left,level+1)
    
    
def getToken(tokenList, expected):
    if tokenList[0] == expected:
        del tokenList[0]
        return True
    else:
        return False
        
def getNumber(tokenList):
    if getToken(tokenList,'('):
        x = getSum(tokenList)
        if not getToken(tokenList,')'):
            raise ValueError, 'missing parenthesis'
        return x
    else:
        x = tokenList[0]
        if not isinstance(x, int):
            return None
#        del tokenList[0]
        tokenList[:1] = []
        return Tree(x, None, None)

def getProduct(tokenList):
    a = getNumber(tokenList)
    if getToken(tokenList,'*'):
        b = getProduct(tokenList)
        return Tree('*',a,b)
    else:
        return a

def getSum(tokenList):
    a = getProduct(tokenList)
    if getToken(tokenList,'+'):
        b = getSum(tokenList)
        return Tree('+', a ,b)
    else:
        return a
        
    
    
    
    
    
    
    