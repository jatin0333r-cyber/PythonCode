def fib(n):
	return n if n < 2 else fib(n-1) + fib(n-2)

k = int(input("Terms: "))
for i in range(k):
	print(fib(i), end=" ")
print()
