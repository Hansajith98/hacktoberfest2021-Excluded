"""You can check all permutaion start with 1 to n
    just like
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
"""
import copy
def permutation(num_list,removed_nums):
    if len(num_list) == 1:
        print(removed_nums + num_list)
        return

    for i in num_list:
        list_copy = copy.deepcopy(num_list)
        permutation(list_copy.replace(i,''), removed_nums + i + " ")

#input the number of n
num_list = [str(i) for i in range(1 , int(input("input n: ")) + 1)]
num_list = ''.join(num_list)
permutation(num_list,"")
