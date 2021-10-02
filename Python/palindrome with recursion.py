def palindrome(s):
  if len(s)==0 or len(s)==1:
    return True
  else:
    if s[0]==s[-1]:
      return palindrome(s[1:-1])      
    else:
      return False

s=input("Enter a String")
if palindrome(s):
  print("It is a Palindrome")
else:
  print("It is not a Palindrome")

