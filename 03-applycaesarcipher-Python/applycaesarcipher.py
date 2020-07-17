# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	sum=''
	if shift >0:
		for i in msg:
			if i == ' ':
				sum = sum+i
			elif i.isupper():
				if (ord(i)+shift)<91:
					sum =sum+chr(ord(i)+shift)
				else:
					sum = sum + chr(ord(i)+shift-26)
			else:
				if (ord(i)+shift)<123:
					sum =sum+chr(ord(i)+shift)
				else:
					sum = sum + chr(ord(i)+shift-26)
		return sum		
	if shift <0:
		for i in msg:
			if i == ' ':
				sum = sum+i
			elif i.isupper():
				if (ord(i)+shift)>65:
					sum =sum+chr(ord(i)+shift)
				else:
					sum = sum + chr(ord(i)+shift-26)
			else:
				if (ord(i)+shift)<123:
					sum =sum+chr(ord(i)+shift)
				else:
					sum = sum + chr(ord(i)+shift-26)
		return sum
	




