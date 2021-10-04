n=int(input("Enter number:"))
a, b = 0, 1
for i in range(n-1):
    a,b=b,a+b
print(a)

def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(n-1))
