# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 10:44:08 2012

@author: yuege
"""

def printMultiples(n,k):
    i = 1
    while i <= k:
        print n*i, '\t',
        i = i + 1
    print
    
def printTables(high):
    i = 1
    while i <= high:
        printMultiples(i,i)
        i = i + 1
    