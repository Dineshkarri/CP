# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n=abs(n)
	c=1
	l=[]
	while (n>0):
		temp=n%10
		n=n//10
		if n%10 == temp:
			c+=1
		else:
			l.append((temp,c))
			c=1
	l.sort(key=lambda x:x[1])
	return l[0][1]