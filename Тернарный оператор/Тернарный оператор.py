# Выражение_1 if Условие else Выражение_2

# Если условие правдиво, тогда возвращается результат Выражения_1
# Если условие ложно, тогда возвращается рузельтат Выражения_2

# ПРИМЕРЫ

my_number = 21.5

print("is int") if type(my_number) is int else print("is not int")
# is not int

print(type(my_number))
# <class 'float'>
# ______________________

product_qty = 10

print("in stock" if product_qty > 0 else "out of stock")
# in stock

# ______________________

temp = +24

weather = "hot" if temp > 18 else "cold"
print(weather)
# hot
