# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

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
	if n>2:
		l.append(n)
	return l
def isugly(n):
	l=primeFactors(n)
	for i in l:
		if i!=2 and i!=3 and i!=5:
			return False
	return True

def fun_nth_uglynumber(n):
	# if n==0:
	# 	return 1
	L=[1]
	j=2
	while(len(L)<=n+1):
		if isugly(j):
			L.append(j)
		j+=1
	print(L)
	# return L[n-1]
