# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

import math
from math import sqrt

def fun_distance(x1, y1, x2, y2):
	dis = sqrt((y2-y1)**2 + (x2-x1)**2)
	return (dis)

def trianglearea(s1, s2, s3):
	s = (s1 +s2 +s3)/2
	return sqrt(s*(s-s1)*(s-s2)*(s-s3))

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = fun_distance(x1,y1,x3,y3)
	b = fun_distance(x2,y2,x3,y3)
	c = fun_distance(x1,y1,x2,y2)
	return trianglearea(a,b,c)