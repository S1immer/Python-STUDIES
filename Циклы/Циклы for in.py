# # for in для списков (list)

# my_list = [True, 10, 'abc', {}]

# for elem in my_list:
#     print(elem)
# # True
# # 10
# # abc
# # {}
# # ____________________________________

# # for in для кортежей (tuple)

# video_info = ('1920x1080', True, 27)

# for elem in video_info:
#     print(elem)
# # 1920x1080
# # True
# # 27
# # ____________________________________

# # for in для словарей (dict)

# my_object = {
#     'x': 10,
#     'y': True,
#     'z': 'abc'
# }

# for key in my_object:
#     print(key, my_object[key])
# # x 10
# # y True
# # z abc
# # ____________________________________

# # Практика

# for el in [1, 'abc', True]:
#     print(type(el))
#     print(el)
# # <class 'int'>
# # 1
# # <class 'str'>
# # abc
# # <class 'bool'>
# # True
# # ____________________________________

# Задача №1


def dict_to_list(input_dict):
    result_list = []
    for key, value in input_dict.items():
        if isinstance(value, int):
            value *= 2

        result_list.append((key, value))
    return result_list


my_dict = {'a': 10, 'b': 15, 'c': 5.5, 'd': 'string'}
result = dict_to_list(my_dict)
print(result)
# [('a', 20), ('b', 30), ('c', 5.5), ('d', 'string')]


def dict_to_list(input_dict):
    new_list = []
    for k, v in input_dict.items():
        if isinstance(v, int):

            new_list.append(v * 2)
    return new_list


print(dict_to_list({'a': 10, 'b': 15, 'c': 5.5, 'd': 'string'}))
# [20, 30]


def dict_to_list(input_dict):
    return [value * 2 if isinstance(value, int) else value for value in input_dict.values()]


print(dict_to_list({'a': 10, 'b': 15, 'c': 5.5, 'd': 'string'}))
# [20, 30, 5.5, 'string']


# ЗАДАЧА №2


# Из функции достаем 'строки' 'str', целые числа int, булевые значения bool
def filter_list(input_list, data_type):
    filtered_list = []
    for item in input_list:
        if isinstance(item, data_type):
            filtered_list.append(item)
    return filtered_list


my_list = ['a', 124, True, '14', 'Hi', False, 15, 124, 15, 'Gold', 'Man']

new_list = filter_list(my_list, str)
print(new_list)
# ['a', '14', 'Hi', 'Gold', 'Man']

new_list = filter_list(my_list, bool)
print(new_list)
# [True, False]

new_list = filter_list(my_list, int)
print(new_list)
# [124, True, False, 15, 124, 15]


# УПРОЩЕННЫЙ вариант с помощью filter

# Определяем список слов
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Определяем функцию-фильтр для слов, начинающихся на букву 'b'


def starts_with_b(word):
    return word.startswith("b")


# Фильтруем слова, начинающиеся на 'b'
filtered_words = filter(starts_with_b, words)

# Преобразуем результат в список
filtered_words_list = list(filtered_words)

# Выводим отфильтрованные слова
print(filtered_words_list)  # Вывод: ['banana']
