# Пробная задача
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9]

result = my_list1 + my_list2

print(type(result))
# Не законченная задача


list1 = [1, 2, 3]
list2 = [4, 5,]


result = list.__add__(list1, list2)

print(result)
print(type(result))

list1 = list2.__add__(result)
print(result)

print(list1)
# Готовая задача

# ЗАДАЧА 1
my_list1 = [1, 2, 3, 4, 5]

del my_list1[3]

print(len(my_list1))

my_list1.reverse()
print(my_list1)

my_list2 = [9, 10]
result = my_list1 + my_list2
print(result)
# Готовая задача


# ЗАДАЧА 2
my_list1 = ['abc', 5, 10.5, True, [1]]

del my_list1[2]

print(len(my_list1))

my_list1.reverse()
print(my_list1)

my_list2 = [9, 10]
result = my_list1 + my_list2
print(result)
print(my_list2)
# Готовая задача


# Задача
my_dict = {}

key_1 = input("Please enter key 1: ")
volue_1 = input("Please enter key 1: ")
my_dict[key_1] = volue_1


key_2 = input("Please enter key 2: ")
volue_2 = input("Please enter key 2: ")
my_dict[key_2] = volue_2


key_3 = input("Please enter key 3: ")
volue_3 = input("Please enter key 3: ")
my_dict[key_3] = volue_3
print(my_dict)
# Конец задачи

# __________________________________________________
# Набор Задача
my_int = {12, 24, 36, 48, 'abc'}

other_int = {10, 12, 24, 50}

my_int_list = list(my_int.intersection(other_int))
print(my_int_list)
# ___________________________________________________

my_int = {12, 24, 36, 48, }

my_int.add(200)

other_int = {10, 12, 36, 20}
set = (my_int.intersection(other_int))
set_list = list(set)
print(set_list)
print(my_int)
print(other_int)
