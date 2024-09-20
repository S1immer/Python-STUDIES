my_set = {10, 10, 5, 15, 15}
print(my_set)
print(len(my_set))
# # конец


# НАБОРЫ (все элементы уникальные, не повторяются)
# .add (добавление элементов)
photo_sizes = {'1920x1080', '800x600'}

photo_sizes.add('1024x768')

print(photo_sizes)
# {'1024x768', '1920x1080', '800x600'}
# Конец


# .union (объединение наборов)
photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}

all_sizes = photo_sizes.union(other_sizes)

print(all_sizes)
{'1024x768', '1920x1080', '800x600'}
# Конец


# intersection (пересечение наборов)
photo_s = {'1920x1080', '800x600'}
other_s = {'800x600', '1024x768'}

common_s = photo_s.intersection(other_s)

print(common_s)
# {'800x600'} выводится результат, который есть и в первом и во втором наборе
# Конец


# issubset (один набор включен в другой)
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)

print(res)
# True
# Конец

# Практика
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
# {'f', 'd'}
# {'f', 'd'}
# _____________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection('abcd'))
# {'d'}
# Нашли все одинаковые элементы среди двух наборов
# _____________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.union(other_set))
# {'abc', 'f', 'd', 'a', 'y'}
# Находит все элементы во всех наборах
# _____________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(other_set.issubset(my_set))
# Результат False, потому что в наборе my_set отсутсвует 'a'
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# Если мы уберем из набора other_set 'a', то ответ будет True
# _____________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.difference(other_set))
# {'abc', 'y'}
print(my_set - other_set)
# {'abc', 'y'}
print(my_set & other_set)
# {'d', 'f'}
print(my_set | other_set)
# {'a', 'abc', 'f', 'd', 'y'}  аналог .union
print(my_set.discard('d'))

# ______________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.discard('d'))

print(my_set)
# None
# None
# {'f', 'abc', 'y'}
# Этим методом можно удалять элементы из наборов

# _______________________________________________________

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

my_set.remove('abc')
# .remove удаляет элементы из метода

print(my_set)
# {'d', 'f', 'y'}

# ________________________________________________________

my_set = {'abc', 'd', 'f', 'y'}

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set)
# {'y', 't', 'f', 'd', 'abc'}

print(copied_set)
# {'y', 'f', 'l', 'abc', 'd'}

print(my_set & copied_set)
# {'f', 'y', 'abc', 'd'} нашли общие элементы между оригинальным сетом и скопированным

# ____________________________________________________________

# Симметричная разница в наборах

my_set = {'abc', 'd', 'f', 'y'}

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set.symmetric_difference(copied_set))
# {'t', 'l'} возвращает новое множество, содержащее элементы,
# которые присутствуют только в одном из двух множеств, но не в обоих.

# ________________________________________________________________

a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 't'}

print((a | b) - (a & b))
# {'t', 'y'} возвращает новое множество, содержащее элементы,
# которые присутствуют только в одном из двух множеств, но не в обоих.

# _________________________________________________________________
