# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	l=[100]*26
	for char in s:
		pos=ord(char)
		if not (65<=pos<=91 or 97<=pos<=122):
			continue
		pos-=97
		if pos>0:
			l[pos]=1 if l[pos]==100 else l[pos]+1
		else:
			pos+=32
			l[pos]=1 if l[pos]==100 else l[pos]+1
	ret,count ="",99
	for pos in range(26):
		val=l[pos]
		if val<count:
			ret=char(pos+97)
		elif val==count:
			ret+=chr(pos+97)
	return ret
	# arr = [100] * 26
	# for char in s:
	# 	pos = ord(char)
	# 	if not (65 <= pos <= 91 or 97 <= pos <= 122):
	# 		continue
	# 	pos -= 97
	# 	if pos >= 0:
	# 		arr[pos] = 1 if arr[pos] == 100 else arr[pos] + 1
	# 	else:
	# 		pos += 32
	# 		arr[pos] = 1 if arr[pos] == 100 else arr[pos] + 1

	# ret, count = "", 99
	# for pos in range(26):
	# 	val = arr[pos]
	# 	if val < count:
	# 		count = val
	# 		ret = chr(pos + 97)
	# 	elif val == count:
	# 		ret += chr(pos + 97)

	# return ret	
