# Объединение словарей с помощью ** или |

# Последовательность объединения важна

# button - кнопка

button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}


button = {
    **button_info,
    **button_style
}

print(button)
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

# __________________________________

# Можно сделать то же самое, но с помощью оператора |
button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}


button = button_info | button_style

print(button)
# {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

# _____________________________________

# Если же одинаковые значения в словарях, то
# это означает, что если ключи повторяются,
# значением ключа будет то, которое принадлежит последнему словарю в операции объединения.

button_default = {
    'text': 'Ok',
    'color': 'black',
    'width': 0,
    'height': 0,
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'height': 300
}

button = {
    **button_default,
    **button_style
}

print(button)
# {'text': 'Ok', 'color': 'yellow', 'width': 200, 'height': 300}

# __________________________________________________

# Можно объеденять много словарей

age_1 = {
    'dan': 21
}

age_2 = {
    'dasha': 24
}

age_3 = {
    'jenny': 24
}

age_4 = {
    'alex': 20
}

age_all = {
    **age_2,
    **age_1,
    **age_4,
    **age_3
}

print(age_all)
# {'dasha': 24, 'dan': 21, 'alex': 20, 'jenny': 24}

age_all_2 = age_2 | age_1 | age_4 | age_3
print(age_all_2)
# {'dasha': 24, 'dan': 21, 'alex': 20, 'jenny': 24}
