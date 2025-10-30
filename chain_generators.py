# Write a program to chain generators?

def count_up_to(max):
  count=1
  while count <=max:
    yield count
    count+=1

def squared_numbers(numbers):
  for number in number:
    yield number**2

for square in squared_number(count_up_to(5)):
  print(square) #Output: 1,4,,9,16,25
