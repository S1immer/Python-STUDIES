# print("В возрасте", age + new_city, "лет", name, "планирует жить в новом городе через", new_city, "лет.")
# print("Город:", city)
# print("Возраст:", age)
# print("Имя:", name)
# # Вывод информации
#
# new_city = int(input("Через сколько лет планируете переезд? "))
# city = input("Где Вы живете? ")
# age = int(input("Введите Ваш возраст: "))
# name = input("Введите Ваше имя: ")
# # Получение данных от пользователя


# print(age)
# age += 2
# age = age +1
# age = 21
# # print(f"Привет, {name}!")
# # Приветственное сообщение
#
# # name = input("Введите ваше имя: ")
# # Запрос имени пользователя
# print(str(124))
# print(type(False))
# print(type('avs'))
# print((type(1.5)))
# print(type(2))
# print("Hello from python")
# print('Hello World')







# Запрос значений у пользователя
plasticity = int(input("Введите число пластичности: "))
liquid = float(input("Введите показатель текучести в долях единиц: "))

# Определение типа грунта на основе введенных данных
if 1 <= plasticity <= 7:
    soil_type = "Супесь"
elif 7 < plasticity <= 17:
    soil_type = "Суглинок"
elif plasticity > 17:
    soil_type = "Глина"
else:
    print("Некорректное значение числа пластичности")


# Определение текстуры грунта на основе показателя текучести
if liquid < 0:
    texture = "твердая"
elif 0 <= liquid <= 0.25:
    texture = "полутвердая"
elif 0.25 < liquid <= 0.50:
    texture = "тугопластичная"
elif 0.50 < liquid <= 0.75:
    texture = "мягкопластичная"
elif 0.75 < liquid <= 1:
    texture = "текучепластичная"
else:
    texture = "текучая"

# Вывод типа грунта
print(f"{soil_type} {texture}")

















