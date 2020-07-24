# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(m):
	if m<=1:
		return False
	for i in range (2,m):
		if m%i ==0:
			return False
	return True

def iscp(n):
	n=str(n)
	m=n+n
	for i in range(len(n)):
		if not isprime(int(m[i:i+len(n)])):
			return False
	return True

def nthcircularprime(n):
	# Your code goes here
	x=2
	L=[]
	while(len(L)<=n):
		if iscp(x):
			L.append(x)
	return L[n]

	pass