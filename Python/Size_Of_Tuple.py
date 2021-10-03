# Python3 code to demonstrate working of 
# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
  
# initializing string
test_str = 'Gfg is best . Gfg also has Classes now. \
                Classes help understand better . '
  
# printing original string
print("The original string is : " + str(test_str))
  
# initializing replace mapping 
repl_dict = {'Gfg' :  'It', 'Classes' : 'They' }
  
# Replace duplicate Occurrence in String
# Using split() + enumerate() + loop
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
  
# printing result 
print("The string after replacing : " + str(res)) 
