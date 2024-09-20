# ИНСТРУКЦИЯ if else

# if Условие:
# Блок кода, выполняемый однократно, если Условие правдиво
# else:
# Блок кода, выполняемый однократно, если Условие ложно

my_number = 21.5

if type(my_number) is int:
    # c помощью is можно сравнить два объекта
    print(my_number, "is integer")
else:
    print(my_number, "is not a integer")
    # 21.5 is not a integer

# __________________________________

my_phone = {
    'price': 200,
    'brand': 'Nokia'
}

if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")
# Phone's brand is Nokia
