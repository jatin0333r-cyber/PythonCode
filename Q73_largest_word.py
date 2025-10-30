s = input("Enter text: ").split()
print(max(s, key=len) if s else "")
