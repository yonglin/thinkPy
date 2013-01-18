# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:54:07 2013

@author: yuege
"""

def report(wages):
    students = wages.keys()
    students.sort()
    for student in students:
        print "%-20s %f" %(student,wages[student])
        