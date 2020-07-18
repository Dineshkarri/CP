# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
	if len(a) == 0: return 0
	# x=y=0
	# for i in range(0,len(a),2):
	# 	x=x+a[i]
	# for i in range(1,len(a)+1,2):
	# 	y=x+a[i]
	# return x-y
	a=(sum(a[0::2]))
	print(a)
	b=(sum(a[1::2]))
	print(b)
	
	return a-b


