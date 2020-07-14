# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		n1 = str(n)
		n2 =n1[::-1]
		list1 = list(n2)
		if k<= len(list1):
			list1.extend(str(d))
		list1[k] = d
		n3 = ''.join(map(str,list1))
		n4 = n3[::-1]
		return int(n4) if n>0 else -int(n4)

