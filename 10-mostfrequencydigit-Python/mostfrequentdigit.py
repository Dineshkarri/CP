# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n =abs(n)
	if n==0:
		return 0
	# n =str(n)
	# temp =0
	# x=0
	# for i in n:
	# 	num =i
	# 	x =n.count(i)
	# 	if x >temp:
	# 		num = i
	# 		temp=x
	# return int(num)
	dic={}
	# lis=[]
	count=0
	num=0
	while n!=0:
		num = n%10
		if num in dic.keys():
			dic[num] +=1
		else:
			dic[num]=1
		n = n//10
	# value = max(dic.values())
	for i in dic.keys():
		if dic[i] > count:
			count = dic[i]
			num = i
		elif dic[i] == count and i<num:
			num = i
	return num
		# if dic[i]==value:
		# 	lis.append(i)
	# return min(lis)