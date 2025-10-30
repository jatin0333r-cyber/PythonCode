c = input("Enter char: ")
print("Uppercase" if c.isalpha() and c.isupper() else "Lowercase" if c.isalpha() and c.islower() else "Not an alphabet")
