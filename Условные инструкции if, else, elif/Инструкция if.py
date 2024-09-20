# Ложные значения
# dict {}
# list []
# tuple ()
# set set()
# range range(0)
# str ""
# __________________
# int 0
# float 0.0
# complex 0j
# __________________
# bool False
# NoneType None
# __________________


# Отдельно if пишется, если введенные значения правдивые

# if условие:
#     операция
# Если нам нужно выполнить операцию только в том случае, если условие истинно, и нам не
# нужно никаких дополнительных действий, мы можем написать простое условие без else или elif.

# Пример
# if x > 5:
#     print("x больше 5")

# Если нам нужно выполнить операцию только в том случае, если условие ложно, мы можем
# использовать конструкцию с not.

# if not x:
#     print("x равно False")


my_number = 25
if my_number > 0:
    print(my_number, "is positive number")
    # 25 is positive number
# _______________________________________

# ПРИМЕР IF С ОПЕРАТОРОМ ОТРИЦАНИЯ NOT

# Эта функция создана для того, чтобы выявить есть ли в словаре 'name',
# если в словаре нет 'name', то оператор not выполняет print("Имя отсутсвует")
person_info = {
    'age': 20
}

if not person_info.get('name'):
    # Действие в случаях, если:
    # 1. Ключа "name" у объекта "person" нет
    # 2. Ключ "name" есть, но его значение ложно
    print("Имя отсутсвует")
# _____________________________________________

num_one = 10
num_two = 5

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):
    print("Both numbers are ints and positive")
