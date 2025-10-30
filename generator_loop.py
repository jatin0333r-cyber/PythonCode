# Write a program to use a generator with a loop?

def fibonacci(n):
  a,b=0,1
  while a<n:
    yied a
    a,b=b,a+b

for num in fibonacci(10):
  print(num) #Output: 0,1,1,2,3,5,8
