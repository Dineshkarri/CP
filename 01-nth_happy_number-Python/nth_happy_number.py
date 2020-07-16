# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

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

def fun_nth_happy_number(n):
	m =1
	list1=[1]
	while n>len(list1):
		if a==ishappynumber(m):
			list1.append(m)
		m +=1
	return list1[n-1]
		
