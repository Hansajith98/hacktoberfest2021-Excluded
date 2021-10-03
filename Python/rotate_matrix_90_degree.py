'''
Rotate matrix 90 degree
123    741
456 ==>852
789    963
'''
import numpy

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# method 1
myArray = numpy.array(matrix)

print(numpy.rot90(myArray, len(myArray)))


# method 2
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i - 1][layer]

            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            matrix[i][- layer - 1] = top
    return matrix


print(rotate_matrix(myArray))
