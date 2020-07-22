# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.
import math
def fun_carrylessadd(x, y):
	sum=0
	total=0
	place=1
	while(x>0 or y>0):
		sum=((x%10)+(y%10))
		if sum>=10:
			sum=sum%10
		total=(sum*place)+total
		# x=math.floor(x/10)
		# y=math.floor(y/10)
		x=x//10
		y=y//10
		place=place*10
		print (total)
	return total
fun_carrylessadd(1,2)
