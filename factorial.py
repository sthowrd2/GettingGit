## Simple python program to test out using Git

def factorial(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return n*factorial(n-1)

def factorial2(n):
	result=1
	while n>0:
		result*=n
		n=n-1
	return result	
	
def binomial(p,q):
	return factorial2(p)/(factorial(q)*factorial2(p-q))

print(factorial(10),factorial2(10))
print(binomial(10,2))
