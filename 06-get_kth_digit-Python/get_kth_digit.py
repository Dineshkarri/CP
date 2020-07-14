# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit1 =abs(digit)
	m = len(str(digit1))
	if m>k:
		for i in range(k+1):
			num = (digit1)%10
			digit = digit1//10
		return num
	return 0
