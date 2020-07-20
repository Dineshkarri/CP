# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.

def fixmostlymagicsquare(L):
	l=[]
	l1=[]
	s=0
	x=sum(L[0])
	for i in L: 
		if sum(i)!=x:
			l.extend(i)
			s=sum(i)
			for j in l:
				if j in i:
					l.append(j)
				else:
					j=j-(s-x)
					l.append(j)
			l1.append(l)
		else:
			l1.append(i)	
	return l1				
	