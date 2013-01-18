# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 18:28:53 2013

@author: yuege
"""
previous={0:1,1:1}
def fib(n):
    if previous.has_key(n):
        return previous[n]
    else:
        newValue = fib(n-1) + fib(n-2)
        previous[n] = newValue
        return newValue