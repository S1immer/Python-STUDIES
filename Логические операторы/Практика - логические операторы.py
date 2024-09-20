# my_list = []

# print(not my_list)  # True


# my_list = [1, 2]

# print(not my_list)  # False


# my_list = [1, 2]

# print(not not my_list)  # True

# # ____________________________________

# my_list = [1, 2]

# other_list = ['a', 'b']

# print(my_list or other_list)
# # [1, 2] получили первый список, потому что выражение с оператором or возвращает первое правдивое значение

# print(len(my_list) < 0 or other_list)
# # ['a', 'b'] получили результат второго списка, потому что первый список ложный

# # ______________________________________

# my_dict = [1, 'a', 10]
# other_dict = [10, 1, 'a']

# my_dict, other_dict == print('dictionaries are equal')
# # dictionaries are equal


# my_dict = [1, 'a', 10]
# other_dict = [10, 1, 'a']

# if my_dict and other_dict:
#     print('dictionaries are equal')
# # dictionaries are equal

my_age = {
    'dan': 21,
    'jenny': 24,
    'daria': 24
}
other_age = {
    'daria': 24,
    'dan': 21,
    'jenny': 24
}

if my_age == other_age and print('dictionaries are equal'):
    pass
# dictionaries are equal

print(bool(my_age == other_age))
# True
