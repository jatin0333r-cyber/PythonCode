n = int(input("Enter n: "))
r = 0
m = abs(n)
while m:
	r = r*10 + m%10
	m //= 10
print(-r if n < 0 else r)
