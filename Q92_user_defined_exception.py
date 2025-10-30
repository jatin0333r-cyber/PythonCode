class MyError(Exception):
	pass

try:
	raise MyError("Something went wrong")
except MyError as e:
	print(e)
