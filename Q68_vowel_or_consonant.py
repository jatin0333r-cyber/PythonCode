c = input("Enter letter: ").lower()
if not c.isalpha() or len(c) != 1:
	print("Invalid")
elif c in "aeiou":
	print("Vowel")
else:
	print("Consonant")
