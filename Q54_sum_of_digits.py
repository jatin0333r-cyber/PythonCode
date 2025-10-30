n = abs(int(input("Enter n: ")))
s = 0
while n:
	s += n % 10
	n //= 10
print(s)
