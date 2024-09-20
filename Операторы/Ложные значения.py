# # Все ложные значения в пайтон
# print(bool(0))  # False
# print(bool(0.0))  # False
# print(bool(0j))  # False


# print(bool(None))  # False

# print(bool({}))  # False
# print(bool([]))  # False
# print(bool(()))  # False
# print(bool(set()))  # False
# print(bool(range(0)))  # False
# print(bool(''))  # False
# # ___________________________

# print(not not {'car': 'priora'})  # True
# print(bool({'car': 'priora'}))  # True

# print(bool({'': []}))  # True

# print(not not {})  # False
# # Двойное отррицание, оператор Not конвертирует всегда значение в ложное значение
# # Not даст нам орицание, а Not Not даст нам оценку, является ложным значение или нет
# # _______________________________________

my_list = [1, 2]
print(len(my_list) > 0)  # True


my_list = []
print(len(my_list) > 0)  # False


my_list = []
print(len(my_list) >= 0)  # True

# ______________________________________________

my_list = [1, 2]

if len(my_list) > 0:
    print("List has elements")  # List has elements


my_list = [1, 2]

if my_list:
    print("List has elements")  # List has elements
