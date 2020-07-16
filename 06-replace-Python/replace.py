# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	# return s1.replace(s2, s3)
	a=len(s2)
	for i in range(len(s1)):
		if s1[i:i+a] == s2:
			s= s +s3
			i = i+a
		else :
			s = s+i

