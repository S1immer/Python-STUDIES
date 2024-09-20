fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]

fruits_qtys_zip = zip(fruits, quantities)

print(fruits_qtys_zip)
# <zip object at 0x00000203A1567540>

print(type(fruits_qtys_zip))
# <class 'zip'>

fruits_qtys_list = list(fruits_qtys_zip)

print(fruits_qtys_list)
# [('apple', 100), ('banana', 70), ('lime', 50)]

# _______________________________________________________

fruits = ['apple', 'banana', 'lime']

quantities = [100, 70, 50]

availability = [True, False, False, True]

fruits_qtys_zip = zip(fruits, quantities, availability)

fruits_qtys_list = list(fruits_qtys_zip)
print(fruits_qtys_list)
# [('apple', 100, True), ('banana', 70, False), ('lime', 50, False)]


# __________________________________________________________


# Конвертация zip объекта в dict

login = ['dan2412dan', 'daniil2002', 'chernya']
password = [516, 326, 174]

key_zip = zip(login, password)

key_dict = dict(key_zip)
print(key_dict)
# {'dan2412dan': 516, 'daniil2002': 326, 'chernya': 174}
# При создании словаря (dict), должно быть не более 2 списков (login, password), иначе пайтон не сможет понять, как составить словарь

# ______________________________________________________


goods = ['Fish', 'Chiken', 'Vegetables', 'Fruits']
prices = [300, 450, 250, 200]

goods_and_prices_zip = zip(goods, prices)
goods_and_prices_dict = dict(goods_and_prices_zip)

print(goods_and_prices_dict)
# {'Fish': 300, 'Chiken': 450, 'Vegetables': 250, 'Fruits': 200}

# _________________________________________________________
