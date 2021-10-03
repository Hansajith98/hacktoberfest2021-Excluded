# Python program to demonstrate working of extended
# Euclidean Algorithm
	
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
	# Base Case
	if a == 0:
		return b,0,1
			
	else:
	    gcd, x, y = gcdExtended(b % a, a)
	    return gcd, y - (b // a) * x, x

 
#  from here execution starts
# Driver code
if __name__ == '__main__':
    print("ax + by = gcd(a, b)") # this is what we have to do
    # taking input from the user 
    m = int(input("Enter the first number: "))  
    n = int(input("Enter the second number: "))  
    # invoking the function
    gcd, x, y = gcdExtended(m, n)
    print("The gcd or hcf is: ", gcd)
    # using fstring
    print(f"x = {x}, y = {y}")
