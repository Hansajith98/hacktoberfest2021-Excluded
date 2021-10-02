num1 = int(input("Enter the number: "))
temp = num1
reverse = 0

while num1 >0:
  remainder = num1 %10
  reverse = (reverse*10) + remainder
  num1 = num1//10
  
if temp == reverse:
  print("The given number is a palindrome")

else:
  print("The number is not a palindrome")