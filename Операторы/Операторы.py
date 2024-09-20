set_one = {10, 'abc', 50, True}
set_two = {'abc', 10, 50, True}

# True       Сравнивает значение {10, 'abc', 50, True}
print(set_one == set_two)
print(set_one.__eq__(set_two))  # True


print(set_one is set_two)  # False
# Сравнивает объекты (сравнивает ссылки(id) местоположения в памяти) set_one и set_two

# С помощью in мы можем проверять есть ли определенный элемент в определенной последовательности
print('abc' in set_one)  # True
print('abc' in set_two)  # True
print(1000 in set_one)  # False


# ___________________________________________


# set1 = [1, 2, 3, 4, 5]
# set2 = [1, 2, 3, 4, 5]

# print(set1 == set2)


# print(set1 is set2)


# print(1 in set1)
