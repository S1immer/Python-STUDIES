# Решение №1
while True:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
        num1 = float(num1)
        num2 = float(num2)
        if num2 != 0:
            result = num1 / num2
            print("Результат деления первого числа на второе:", result)
        else:
            print("Ошибка: Второе число не должно быть нулем.")
    else:
        print("Ошибка: Пожалуйста, введите числовые значения.")

    choice = input("Хотите продолжить? (yes/no): ")
    if choice.lower() != 'yes':
        break

# Решение №2
while True:
    try:
        nun_one = float(print("Please enter number one: "))
        num_two = float(print("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(nun_one / num_two)

    answer = input("Do you wsnt to continue? (yes/no): ")
    if answer == 'no':
        break

# Решение №3
# Самое удобное решение
while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        result = num1 / num2
        print("Результат деления:", result)
        choice = input("Хотите продолжить? (yes/no): ")
        if choice.lower() == "no":
            break
    except ValueError:
        print("Ошибка: Введите числа.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
