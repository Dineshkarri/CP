# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def issum(n):
	sum=num=0
	while n>0:
		num = n%10
		sum =sum + num**2
		n=n//10
	return sum

def ishappynumber(n):
	# your code goes here
	lis=[]
	if n<0:
		return False
	while True:
		n = issum(n)
		if n in lis:
			return False
		lis.append(n)
		if n==1:
			return True

def isprime(m):
	for i in range (2,m):
		if m%i ==0:
			return False
	return True

def fun_nth_happy_prime(n):
	m =8
	list1=[7]
	while True:
		if ishappynumber(m):
			if isprime(m):
				list1.append(m)
		m +=1
		if len(list1)==n:
			break
	return list1[n-1]