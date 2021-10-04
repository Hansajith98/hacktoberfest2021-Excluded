data = [635,4,54454,1,8657,8889] #Your List
for i in range(1, len(data)):
    k = data[i]
    j = i - 1       
    while j >= 0 and k < data[j]:
        data[j + 1] = data[j]
        j = j - 1
    data[j + 1] = k

print('Sorted Array:')
print(data)
