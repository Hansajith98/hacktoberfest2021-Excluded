import random
def quicksort(collection):

    for i in range(len(collection)):
        j = random.randint(0, len(collection) - 1)
        tmp = collection[i]
        collection[i] = collection[j]
        collection[j] = tmp
    quicksort_r(collection, 0, len(collection))


def quicksort_r(collection, start, stop):
    if start >= stop - 1:
        return
    pivot_index = partition(collection, start, stop)
    quicksort_r(collection, start, pivot_index)
    quicksort_r(collection, pivot_index + 1, stop)

def partition(collection, start, stop):

    pivot_index = start
    pivot = collection[pivot_index]

    i = start + 1
    j = stop - 1

    while i <= j:
        while i <= j and not pivot < collection[i]:
            i += 1
        while i <= j and pivot < collection[j]:
            j -= 1
        if i < j:
            tmp = collection[i]
            collection[i] = collection[j]
            collection[j] = tmp
            i += 1
            j -= 1
    collection[pivot_index] = collection[j]
    collection[j] = pivot
    return j


l = [6, 2, 13, 8, 9, 0, 1, 7, 5, 3, 6, 17]

quicksort(l)

print(l)
