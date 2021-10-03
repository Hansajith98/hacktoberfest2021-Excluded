arr = [-2,1,-3,4,-1,2,1,-5,4]

current_sum = 0
maximum_sum = 0

for i in arr:
    current_sum = max(current_sum+i,i)
    maximum_sum = max(maximum_sum,current_sum)

print(maximum_sum)