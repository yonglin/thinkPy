# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:48:07 2013

@author: yuege
"""

class Time:
    
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def printTime(t):
        print "%d:%d:%d"%(t.hours,t.minutes,t.seconds)
    
    def convertToSeconds(self):
        minutes = 0
        seconds = 0
        minutes = self.hours * 60 + self.minutes
        seconds = minutes * 60 + self.seconds
        return seconds
#def addTime(t1,t2):
#    sum = Time()
#    sum.hours = t1.hours + t2.hours
#    sum.minutes = t1.minutes + t2.minutes
#    sum.seconds = t1.seconds + t2.seconds
#    return sum


    

    
def makeTime(seconds):
    time = Time()
    time.hours = seconds // 3600
    time.minutes = (seconds % 3600) // 60
    time.seconds = seconds % 60
    return time
    
def addTime(t1,t2):
    seconds = convertToSeconds(t1) + convertToSeconds(t2)
    return makeTime(seconds)