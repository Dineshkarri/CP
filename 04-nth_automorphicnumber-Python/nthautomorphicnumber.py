# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.
def isamn(n):
	sq=n**2
	while(n>0):
		if (sq % 10)!= (n % 10):
			return False
		n=n//10
		sq=sq//10
	return False
	

def nthautomorphicnumbers(n):
	# Your code goes here
	L=[0,0,1]
	j=4
	while(len(L)<=n):
		if isamn(j):
			L.append(j)
		j+=1
	return L[n]
	pass