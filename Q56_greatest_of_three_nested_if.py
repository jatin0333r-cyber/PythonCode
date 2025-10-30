a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b:
	m = a if a >= c else c
else:
	m = b if b >= c else c
print(m)
