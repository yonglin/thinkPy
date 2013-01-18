# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:29:23 2013

@author: yuege
"""

def inputNumber():
    x = input('Pick a number:')
    if x == 17:
        raise ValueError, "17 is a bad number"
    return x
    