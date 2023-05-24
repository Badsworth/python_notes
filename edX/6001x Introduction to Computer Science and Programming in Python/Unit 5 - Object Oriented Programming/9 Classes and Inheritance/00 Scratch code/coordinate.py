# -*- coding: utf-8 -*-
"""
Created on Tue May 10 08:18:02 2016

@author: WELG
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)


'''
__init__ special menthod to create an instance __ is double underscore

think of c as pointing to a frame (like we saw with function calls
    within the scope of that frame we bound values to data attribute varaiables

    c.x is interpreted as getting the value of c (a frame) and
    then looking up the value associated with x within that frame
    (thus the specific value for this instance)
'''
c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(c.x)
print(origin.x)
c
print(c.distance(origin))
