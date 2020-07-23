# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

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
	if m<=1:
		return False
	for i in range (2,m):
		if m%i ==0:
			return False
	return True

def ishappyprimenumber(n):
	# Your code goes here
		if ishappynumber(n):
			if isprime(m):
				return True
		return False