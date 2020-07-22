# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
l=[]
import math
def primeFactors(n):
	while n % 2 == 0: 
		l.append(2) 
		n = n // 2
	for i in range(3,int(math.sqrt(n))+1,2):
		while n % i== 0:
			l.append(i)
			n = n // i 
	if n > 2:
		l.append(n)
	return(l)

def issmith(n):
	a=n
	n=sum(list(str(n)))
	# for y in n:
	# 	a+=int(y)
	x=primeFactors(a)
	for i in x:
		if len(str(i))>1:
			i=sum(list(str(i)))
	b=sum(x)
	if a==b:
		return True
	return False
L=[]	
def fun_nth_smithnumber(n):
	j=0
	while(len(L)<=n):
		if issmith(j):
			L.append(j)
		j+1
	return L[n]