n = int(input("Enter n: "))
s = 0
m = n
d = len(str(n))
while m:
	s += (m % 10) ** d
	m //= 10
print("Armstrong" if s == n else "Not Armstrong")
