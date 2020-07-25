# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
def isamn(n):
	sqrt=n**2
	m=len(str(n))
	num=sqrt%(10**m)
	return n==num

def nthautomorphicnumbers(n):
	# Your code goes here
	L=[0,0,1]
	j=4
	while(len(L)<=n):
		if isamn(j):
			L.append(j)
	return L[n]
	pass