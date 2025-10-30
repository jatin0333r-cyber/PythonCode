n = int(input("Enter n: "))
s = str(abs(n))
print("Palindrome" if s == s[::-1] and n >= 0 else "Not Palindrome")
