# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
from math import sqrt
def isperfectsquare(n):
	# your code goes here
	if type(n) != int:
		return False
	# for i in range (n):
	# 	if i*i == n:
	# 		return True
	# return False
	# if type(n) == int and n>0:
		# x = sqrt(n)
	return ((sqrt(n) - math.floor(sqrt(n))) == 0) if n>0 else False
	# 	if type(x) == int:
	# 		return True
	# return False
