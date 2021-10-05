rows = int(input("Enter you number:"))
n = 0
for i in range(1, rows + 1):
    n = 0

    # loop to print spaces
    n = (rows - i)
    print(" " * n, end = "")

    # loop to print star
    n = (2 * i - 1)
    print(str(i) * n, end = "")
    print()
####
for i in range(rows-1, 0, -1):
    
    # loop to print spaces
    n = (rows - i)
    print(" " * n, end = "")
    
    # loop to print star
    n = (2 * i - 1)
    print(str(i) * n, end ="")
    print()