# Задача №1
my_dict = {
    '79': 'gold',
    '11': 'silver',
    '31': 'bronze'
}

upper_dict = {key: value.upper() for key, value in my_dict.items()}

print(upper_dict)
# {'79': 'GOLD', '11': 'SILVER', '31': 'BRONZE'}

# Задача №2
to_list = ['ch', 'jenny', 'my', 'dasha', 52, 63]

result_list = [elem for elem in to_list if len(str(elem)) < 3]

print(result_list)
# ['ch', 'my', 52, 63]
