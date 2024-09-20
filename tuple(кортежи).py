new_fruits = (151, 253, 633, 346)


if (new_fruits):
    print(new_fruits[1] > new_fruits[-1])

else:
    (new_fruits)
print(new_fruits[1] < new_fruits[-1])

print(len(new_fruits))
# конец


num = (142, 124, 156, 142, 111)

num_new_list = list(num)
num_new_list.append(2424)

print(num_new_list)

num_new_tuple = tuple(num_new_list)
print(num_new_tuple)
# конец


my_nums = (10, 5, 100, 0, 5, 5)

my_list = list(my_nums)

my_list.append(7)

modified_tuple = tuple(my_list)

print(modified_tuple)
# конец


my_tuple = (10, 'abc', True)

my_tuple_two = ({'dan': 1, 'dasha': 2})

result = tuple(my_tuple) + tuple(my_tuple_two)
print(result)
# конец
