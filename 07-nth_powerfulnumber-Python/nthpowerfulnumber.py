# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def primeFactors(n):
	l=[]
	m=n
	while n % 2 == 0: 
		l.append(2) 
		n = n // 2
	for i in range(3,m,2):
		while n % i== 0:
			l.append(i)
			n = n // i
	return l

def ispn(j):
	l=primeFactors(j)
	if len(l)==0:
		return False
	for i in l:
		if j%(i**2)!=0:
			return False
	return True
	
def nthpowerfulnumber(n):
	# Your code goes here
	if n==0:
		return 1
	L=[]
	j=2
	while(len(L)<=n):
		if ispn(j):
			L.append(j)
		j+=1
	print(L)
	return L[n-1]

	
