# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def factorial(n):
	num=1
	if n == 0:
		return 1
	for i in range(1,n+1):
		num= num*i
	return num
def fun_pascaltrianglevalue(row, col):
	return factorial(row)//(factorial(col)*factorial(row-col))