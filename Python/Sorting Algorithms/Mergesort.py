def mergesort(collection):
    mergesort_recursively(collection, 0, len(collection))


def mergesort_recursively(collection, start, stop):

    if start >= stop - 1:
        return

    mid = (start + stop) // 2
    mergesort_recursively(collection, start, mid)
    mergesort_recursively(collection, mid, stop)
    merge(collection, start, mid, stop)


def merge(collection, start, mid, stop):
    li = []
    i = start
    j = mid

    while i < mid and j < stop:
        if collection[i] < collection[j]:
            li.append(collection[i])
            i += 1
        else:
            li.append(collection[j])
            j += 1

    while i < mid:
        li.append(collection[i])
        i += 1

    for i in range(len(li)):
        collection[start + i] = li[i]
