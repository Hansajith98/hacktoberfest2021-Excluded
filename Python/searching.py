def linear_search(liner_list):
	print('\n<<<<<<<<<< THIS IS LINEAR SEARCHING >>>>>>>>>>')
	linear_val = int(input('\nEnter the value you want to search :: '))
	linear = 0

	for i in range(len(liner_list)):
		if linear_val == liner_list[i]:
			print(f'\nThe value ->{linear_val}<- found at position -->>{i + 1}<<-- of list')
			linear = 1
			break
	if linear != 1:
		print(f'\n The element ->{linear_val}<- not found in list')


def binary_search(binary_list):
	print('\n<<<<<<<<< THIS IS BINARY SEARCHING >>>>>>>>>>')

	binary_list.sort()
	print('The sorted list is :: ', binary_list)

	num = int(input('\nEnter the number you want to search :: '))

	first = 0
	last = len(raw_list) - 1
	middle = 0

	while(first <= last):

		middle = (first + last) // 2

		if binary_list[middle] < num:
			first = middle + 1

		elif binary_list[middle] == num:
			print(f'\nThe element ->{num}<- found at location -->>{middle + 1}<<-- in list')
			break

		else:
			last = middle - 1

		middle = first + last // 2

	if first > last:
		print(f'The element ->{num}<- not found in list')


def wrong(new_list):
	print(f'\nYou have entered wrong choice, So you cannot search in list {new_list}')


def dict_switch(sel_choice):
	raw_dict = {
		1: linear_search,
		2: binary_search
	}

	return raw_dict.get(sel_choice, wrong)(raw_list)


raw_list = []
value = int(input('Enter the number of values in list :: '))

for i in range(value):
	list_val = int(input(f'Enter the value {i + 1} in list :: '))
	raw_list.append(list_val)

print('\nThe list is :: ', raw_list)


print("""
	1. Enter ->1<- for LINEAR SEARCHING
	2. Enter ->2<- for BINARY SEARCHING""")

choice = int(input('\nEnter your Choice ::'))
dict_switch(choice)
