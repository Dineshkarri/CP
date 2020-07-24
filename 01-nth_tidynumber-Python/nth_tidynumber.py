# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidy(n):
	while(n>0):
		nu=0
		num=n%10
		n=n//10
		if num < nu:
			return False
		nu=num
	return True
		
def fun_nth_tidynumber(n):
	L=[]
	j=1
	while(len(L)<=n):
		if istidy(j):
			L.append(j)
		j+=1
	print(L)
	return L[n]