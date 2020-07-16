# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	a = len(str2)
	if len(str1) != len(str2): return False
	s =str1+str1
	for i in range(len(s)):
		if s[i:i+len(str2)]==str2 or s[i:i+len(str2)]==str2[::-1]:
			return True
	return False
	pass