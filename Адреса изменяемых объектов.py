my_list = [1, 2, 3]
print(id(my_list))
# 1747291003136

other_list = [1, 2, 3]
print(id(other_list))
# 2041743266176

print(id([1, 2, 3]))
# 2083436374272

# _______________________________

my_list = [1, 2, 3]
other_list = [1, 2, 3]
other_list.append(4)               # .append(4) Добавляет цифру в список

print(my_list)
# [1, 2, 3]

print(other_list)
# [1, 2, 3, 4]

# __________________________________
