# Sorting Algorithm: Insertion Sort
# Time Complexity: O(n^2) , where n is the no of elements
# Space Complexity: O(1)

def insertionSort(arr):
    print(f"Unsorted Array: {arr}")
    # Size of Array
    size = len(arr)
    shifts = 0
    i = 1
    while i <= size-1:
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            shifts+=1
        arr[j + 1] = key
        i = i + 1
        print(f"{arr}")
    print(f"Steps: {i} \t Shifts: {shifts}")
    return arr

a = [2,6,9,4,8,1,5,7]
sorted_arr = insertionSort(a)
print(f"Sorted Array is: {sorted_arr}")