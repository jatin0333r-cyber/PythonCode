a = int(input("Base: "))
b = int(input("Exp: "))
r = 1
for _ in range(b):
	r *= a
print(r)
