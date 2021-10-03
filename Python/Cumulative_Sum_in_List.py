def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
 
# Driver Code
lists = [10, 20, 30, 40, 50]
print (Cumulative(lists))
