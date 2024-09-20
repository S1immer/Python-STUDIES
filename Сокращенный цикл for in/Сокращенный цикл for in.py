# Обычный цикл for in
all_nums = [-3, 1, 0, 10, -20, 5]
absolut_nums = []

for num in all_nums:
    absolut_nums.append(abs(num))

print(absolut_nums)
# [3, 1, 0, 10, 20, 5]
print(all_nums)
# [-3, 1, 0, 10, -20, 5]


# Скоращенный for in для списков (list)
all_nums = [-3, 1, 0, 10, -20, 5]

absolut_nums = [abs(num) for num in all_nums]

print(absolut_nums)
# [3, 1, 0, 10, 20, 5]
print(all_nums)
# [-3, 1, 0, 10, -20, 5]


# Формирование нового списка с фильтрацией в обычном for in
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = []
for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)
# [1, 10, 5]
print(all_nums)
# [-3, 1, 0, 10, -20, 5]


# Скоращенный for in с фильтрацией для списков (list)
all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
# [1, 10, 5]
print(all_nums)
# [-3, 1, 0, 10, -20, 5]
