# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def ispd(n):
	n=str(n)
	return n==n[::-1]

def isln(n):
	j=0
	while j<20:
		n=str(n)
		n=int(n)+int(n[::-1])
		if ispd(n):
			return False
		j+=1
	return True
def nthlychrelnumbers(n):
	# your code goes here
	L=[]
	i=196
	while(len(L)<=n):
		if isln(i):
			L.append(i)
		i+=1
	return L[n-1]