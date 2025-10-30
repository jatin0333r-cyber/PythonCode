s = input("Enter text: ").lower()
v = sum(1 for c in s if c in "aeiou")
c = sum(1 for c in s if c.isalpha()) - v
print("Vowels:", v, "Consonants:", max(c, 0))
