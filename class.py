# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:14:50 2013

@author: yuege
"""

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
#       print '(%d,%d)' % (self.x, self.y)
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
        
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __rmul__(self, other):
        return Point(other * self.x, other * self.y)
    
    def reverse(self):
        self.x , self,y = self.y , self.x
class Rectangle:
    pass

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0
    return p



def samePoint(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

def growRect(box,dwidth,dheight):
    import copy
    newBox = copy.deepcopy(box)
    newBox.width = newBox.width + dwidth
    newBox.height = newBox.height + dheight
    return newBox
