# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def su(l,i,s1):
	if i==len(l):
		return s1
	if i%2==0:
 		s1=s1+l[i]
	else:
		s1=s1-l[i]
	return su(l,i+1,s1)

def fun_recursions_alternatingsum(l):
	if len(l) == 0:return 0
	return 0
	i,s1=0,0
	return su(l,i,s1)
	 

# for i in range(0,len(l)):
# 	if i%2==0:
# 		s1=s1+l[i]
# 	else:
# 		s1=s1-l[i]
# return s1