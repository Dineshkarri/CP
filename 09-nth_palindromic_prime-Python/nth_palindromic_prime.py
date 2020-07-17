# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def isprime(m):
	for i in range (2,m):
		if m%i ==0:
			return False
	return True
	
def ispd(n):
	n=str(n)
	if n[::]==n[::-1]:
		return True
	return False

def fun_nth_palindromic_prime(n):
	if n==0:
		return 2
	m =3
	list1=[]
	while True:
		if ispd(m):
			if isprime(m):
				list1.append(m)
		m +=1
		if len(list1)==n+1:
			break
	return list1[len(list1)-1]