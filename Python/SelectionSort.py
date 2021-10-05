# SELCTION SORT
""" IT HAS A TIME COMPLEXITY OF O(n^2) WHICH IS PRETTY SLOW AS COMPARED TO BINARY SEARCH AND QUICK SORT
"""
def findSmallest(array):
    smallest = array[0]    #Stores the smallest value
    smallest_index = 0     #Stores the index of the smallest value
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index
#Now you can use this function to write selection sort:
def selectionSort(array):   #Sorts an array
    newArr = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        newArr.append(array.pop(smallest))
    return newArr
print(selectionSort([5,-90,687,33,450,0,90,23,-567,343,12300,999]))
