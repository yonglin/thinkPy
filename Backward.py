# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:19:30 2012

@author: yuege
"""
def printBack(s):
    i = len(s)-1
    while i >= 0:
        print s[i]
        i-=1

def find(str,ch,index):
    while index < len(str):
        if str[index] == ch:
            return index
        index += 1
    return -1
    
def countChar(target,string):
    count = 0
    for char in string:
        if char == target:
            count += 1
    print count