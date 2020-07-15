# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n =abs(n)
	n =str(n)
	temp =0
	x=0
	for i in n:
		num =i
		x =n.count(i)
		if x >temp:
			num = i
			temp=x
	return int(num)