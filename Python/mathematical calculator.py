# take two input numbers
number1 = input("Insert first number : ")
number2 = input("Insert second number : ")

operator = input("Insert operator (+ or - or * or /)")

if operator == '+':
    total = number1 + number2
elif operator == '-':
    total = number1 - number2
elif operator == '*':
    total = number2 * number1
elif operator == '/':
    total = number1 / number2
else:
    total = "invalid operator"


# printing output
print(total)