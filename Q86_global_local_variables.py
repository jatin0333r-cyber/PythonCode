x = 10

def change():
	global x
	x = 20
	print("Inside:", x)

print("Before:", x)
change()
print("After:", x)
