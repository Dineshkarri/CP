# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	dic={}
	s=s.replace(" ","")
	for i in s:
		if i not in dic:
			dic[i]=s.count(i)
	# print(dic)
	sort_dic = sorted(dic.values(), reverse=True)
	if len(sort_dic) <n:
		a=sort_dic[0]
		return a[0]
	# print (sort_dic[1])
	for i in range(len(sort_dic)):
		if i == n-1:
			a=sort_dic[i]
			return a[0]
	


