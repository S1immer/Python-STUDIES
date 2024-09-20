my_range = range(10, 20, 3)
print(list(my_range))
for n in my_range:
    print(n)  # [10, 13, 16, 19]
# __________________

my_range = range(5)

for n in my_range:
    print(n)
# 0
# 1
# 2
# 3
# 4

print(my_range[0])  # 0
# __________________

for n in range(5):
    print(n)

# 0
# 1
# 2
# 3
# 4

# __________________

for n in range(12, 25, 5):
    print(n)
# 12
# 17
# 22

# __________________
print(list(range(12, 25, 5)))       # [12, 17, 22]
print(tuple(range(12, 25, 5)))      # (12, 17, 22)
print(set(range(12, 25, 5)))        # {17, 12, 22}

# __________________

my_range = range(10, 30, 3)

print(my_range.start)               # 10 начало диапазона
print(my_range.stop)                # 30 конец диапазона
print(my_range.step)                # 3  шаг дапазона

# __________________

my_range = range(10, 30, 3)

print(my_range.index(13))

# Если число 12 нет в диапазоне, терминал выдаст ответ: 0
print(my_range.count(12))
# Если число 13 будет стоять, терминал выдаст ответ 1
# Т.е. .count выдает ответы только 0, 1, в зависимости есть ли такое число в диапазоне или нет
