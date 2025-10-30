l = int(input("Start: "))
r = int(input("End: "))
for n in range(max(2, l), r+1):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			break
	else:
		print(n)
