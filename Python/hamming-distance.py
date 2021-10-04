# Hamming distance
def hammingDist(v1, v2):
    i = 0
    count = 0
    if len(v1) != len(v2):
        print("Please provide same length of both strings.")
        exit()

    while (i < len(v1)):
        if (v1[i] != v2[i]):
            count += 1
        i += 1
    return count

# Driver code
v1 = input("enter v1: ")
v2 = input("enter v2: ")

# function call
print(hammingDist(v1, v2))
