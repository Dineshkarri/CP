# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math

def fun_distance(x1, y1, x2, y2):
	dis = math.sqrt((y2-y1)**2 + (x2-x1)**2)
	return dis

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = fun_distance(x1,y1,x3,y3)
	b = fun_distance(x2,y2,x3,y3)
	c = fun_distance(x1,y1,x2,y2)
	# d = math.sqrt(b*b+c*c)
	return math.isclose(math.sqrt(b*b+c*c),a)
	
