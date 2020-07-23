# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math
def isprime(m):
	if m<=1:
		return False
	for i in range (2,m):
		if m%i ==0:
			return False
	return True

def truncatePrime(n):
	j=len(str(n))
	i=10
	# for x in range(j):
	# 	if not isprime(n%i):
	# 		return False
	while(True):
		if not isprime(n%i):
			return False
		i=i*10
		if i>10**j:
			break
	return True

def fun_nth_lefttruncatableprime(n):
	m=1
	list1=[]
	while True:
		if truncatePrime(m):
			list1.append(m)
		m +=1
		if len(list1)==n+1:
			break
	print(list1)
	return list1[n]