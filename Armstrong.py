# Write Python code to armstrong Numbers Using Function

def is_amstrong(num):
digits= str(num)
power=len(digits)
total=0

   for digit in digits:
       total +=int(digits)**power
return total==num

#Taking input from users
number=int(input("Enter a number: "))

if is_armstrong(number):
  print(number,"is an armstrong number")
else:
  print(number,"is not an armstrong number")
