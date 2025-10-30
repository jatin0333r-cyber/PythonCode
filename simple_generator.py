# Write a program to create a simple generator?

def count_up_to(max):
  count=1
  while count <=max:
    yield count
    count+=1

for num in count_up_to(5):
  print(num) #output: 1,2,3,4,5
