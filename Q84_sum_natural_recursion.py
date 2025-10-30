def s(n):
	return 0 if n == 0 else n + s(n-1)

print(s(int(input("n: "))))
