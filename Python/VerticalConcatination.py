 #Python3 code to demonstrate working of 
# Vertical Concatenation in Matrix
# Using loop
  
# initializing lists
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
  
# printing original list
print("The original list : " + str(test_list))
  
# using loop for iteration
res = []
N = 0
while N != len(test_list):
    temp = ''
    for idx in test_list:
          
        # checking for valid index / column
        try: temp = temp + idx[N]
        except IndexError: pass
    res.append(temp)
    N = N + 1
  
res = [ele for ele in res if ele]
  
# printing result 
print("List after column Concatenation : " + str(res))
