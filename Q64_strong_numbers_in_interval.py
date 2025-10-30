l = int(input("Start: "))
r = int(input("End: "))
from math import factorial
for n in range(l, r+1):
	if sum(factorial(int(d)) for d in str(n)) == n:
		print(n)
