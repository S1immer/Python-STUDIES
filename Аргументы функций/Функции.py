# a = 5
# b = 3

# c = a + b
# print(c)
# # 8

# a = 8
# b = 12

# c = a + b
# print(c)
# # 20

# # _______________________________________
# # Вместо написанного выше, можно написать другим упрощенным способом ниже


# def sum(a, b):
#     c = a + b
#     print(c)

#     a = 5
#     b = 3

#     sum(a, b)

#     a = 8
#     b = 12

#     sum(a, b)


# print(type(sum))
# # <class 'function'>

# # Функция возвращает None если нет ключевого слова Return

# # Видеоурок 'Функции' №86


# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c


# res = my_fn(10, 3)
# print(res)
# # 14


# def num(a, b, c):
#     a = a + 3  # 13
#     b = a + b  # 17
#     c = c + 4  # 6
#     d = a + b + c  # 13+17+6=36
#     return d


# res = num(10, 4, 2)
# print(res)
# # 36

# # __________________________________

# # Самая короткая функция pass


# def my_fn():
#     pass


# print(my_fn())
# # None
# # Функция возвращает по умолчанию None если в функции нет ключевого слова return

# # ___________________________________

# # Передача неизменяемых объектов


# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c


# num_one = 10
# num_two = 5

# res = my_fn(num_one, num_two)
# print(res)
# # 16
# print(num_one)
# # 10

# # ______________________________________


# def merge_list_to_dict(keys, values):
#     result_dict = dict(zip(keys, values))
#     return result_dict


# keys = ['a', 'b', 'c']
# values = [1, 2, 3]

# result_dict = merge_list_to_dict(keys, values)
# print(result_dict)


# ___________________________________________

# def keys_list(num_one, num_two):
#     return dict(zip(keys_list))


# result = keys_list([1, 2, 3], [{'a'}, True, []])
# print(result)


# def merge_list_to_dict(keys, values):
#     result_dict = dict(zip(keys, values))
#     return result_dict


# words = ['a', 'b', 'c']
# numbs = [1, 2, 3]
# fruits = ['orange', 'apple', 'bananas']

# result_dict = merge_list_to_dict(words, numbs)
# result_dict_two = merge_list_to_dict(fruits, numbs)

# print(result_dict)
# print(result_dict_two)

# _______________________________________________________________________________________________________
def function(x, y):
    result_zip = zip(x, y)
    result_dict = dict(result_zip)
    return result_dict


city = ['Perm', 'Moscow']
people = [100, 200]
#                                                         В принт пишем название функции (function)
#                                                         и в скобках заданные данные для x и y
print(function(city, people))
# {'Perm': 100, 'Moscow': 200}

# _______________________________________________________________________________________________________
