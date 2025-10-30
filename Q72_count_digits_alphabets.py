s = input("Enter text: ")
d = sum(1 for c in s if c.isdigit())
a = sum(1 for c in s if c.isalpha())
print("Digits:", d, "Alphabets:", a)
