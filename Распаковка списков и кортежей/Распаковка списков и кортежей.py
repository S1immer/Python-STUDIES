# Распаковка списков (list)
my_fruits = ['apple', 'banana', 'lime']

my_one, my_two, my_three = my_fruits

print(my_one)
# apple
print(my_two)
# banana
print(my_three)
# lime


my_list = [1, 2, 3]

first, second, third = my_list

print(first)  # 1
print(second)  # 2
print(third)  # 3

# _______________________________

# Распаковка кортежей (tuple)

my_fruits = ('apple', 'banana', 'lime')
print(type(my_fruits))  # <class 'tuple'>

my_apple, my_banana, my_lime = my_fruits

print(my_apple)
# apple
print(my_banana)
# banana
print(my_lime)
# lime

# ___________________________________

# Использование * при распаковке
my_fruits = ('apple', 'banana', 'lime')

my_apple, *remaining_fruits = my_fruits

print(my_apple)
# apple
print(remaining_fruits)
# ['banana', 'lime']

print(type(remaining_fruits))
# <class 'list'>
