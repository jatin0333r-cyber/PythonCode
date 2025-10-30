a = int(input("a: "))
b = int(input("b: "))
from math import gcd
print(abs(a*b)//gcd(a, b))
