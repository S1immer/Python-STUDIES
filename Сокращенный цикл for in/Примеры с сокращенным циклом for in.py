my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)
# {1, 100, 225}
print(my_set)
# {1, 10, 15}


# Сокращенный for in для наборов (set)
my_set = {1, 10, 15}

new_set = {val * val for val in my_set}

print(new_set)
# {1, 100, 225}
print(my_set)
# {1, 10, 15}


# Формирование нового словаря в обычном fot in
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10

print(scores)
# {'a': 100, 'b': 70, 'm': 140}
print(my_scores)
# {'a': 10, 'b': 7, 'm': 14}


# Сокрщенный for in для словарей (dict)
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {k: v * 10 for k, v in my_scores.items()}

print(scores)
# {'a': 100, 'b': 70, 'm': 140}
print(my_scores)
# {'a': 10, 'b': 7, 'm': 14}

# Преобразуем список в словарь, ключ будет индексом [0], [1], [2]
my_scores = [10, 7, 14]

# my_scores = {
#     '0': 10,
#     '1': 7,
#     '2': 14
# }

scores = {index: elem for index, elem in enumerate(my_scores)}

print(scores)
# {0: 10, 1: 7, 2: 14}
