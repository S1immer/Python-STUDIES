# ИНСТРУКЦИЯ if elif

# if Условие_1:
# Блок кода, выполняемый однократно, если Условие_1 правдиво
# elif Условие_2:
# Блок кода, выполняемый однократно, если Условие_1 ложно, а Условие_2 правдиво
# else:
# Блок кода, выполняемый однократно, если предыдущие условия ложны

my_number = -10

if my_number > 0:
    print(my_number, "is positive number")
elif my_number < 0:
    print(my_number, "is negative number")
else:
    print(my_number, "is zero")


# ПРЕДПОЧТИТЕЛЬНЫЙ ФОРМАТ if

# if Условие_1:
# Блок кода, выполняемый однократно, если Условие_1 правдиво

# if Условие_2:
# Блок кода, выполняемый однократно, если Условие_2 правдиво

# if Условие_3:
# Блок кода, выполняемый однократно, если Условие_3 правдиво
