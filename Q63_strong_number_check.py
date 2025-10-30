n = int(input("Enter n: "))
from math import factorial
print("Strong" if sum(factorial(int(d)) for d in str(n)) == n else "Not Strong")
