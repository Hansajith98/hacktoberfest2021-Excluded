def minJumps(arr, n):
       
     
    i=0
    jump=0
        
    while(i<n):
 
        if arr[i]==0:
            return -1
                
        val=arr[i] #maximum number of steps that can be taken currently
        curr_max=0 #initializing the next maxm step
            
        #If we reached to the final step
        if i+arr[i]>=n-1:
            jump+=1
            return jump
                
            
        flag=1
        #Finding the next maximum step
        for j in range(i+1,i+val+1):
            if arr[j]+j>curr_max: 
                curr_max=arr[j]+j
                i=j
                flag=0
            if flag:
                return -1
        jump+=1
    return jump

print("Enter array elements with space")
arr=list(map(int,input().split()))
jump=minJumps(arr,len(arr))
print("Minimum Jumps to reach to end of array :",jump)