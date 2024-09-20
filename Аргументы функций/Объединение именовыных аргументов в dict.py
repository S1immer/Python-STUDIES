# **person представляет собой синтаксис, используемый для передачи именованных аргументов в функцию в виде словаря.

# Этот синтаксис называется "распаковкой словаря" или "распаковкой ключевых аргументов".

# Когда вы передаете **person в качестве аргумента функции, person должен быть словарем.

# Ключи этого словаря будут использоваться как именованные аргументы в вызове функции, а их значения будут переданы как значения этих аргументов.

# (**person) работает только с именованными аргументами (posts_qty=30, name='Dan')
# (**person) объеденила и создала словарь из (name='Dan', posts_qty=30)

# ___________________________________________________________

def get_posts_info(**person):
    print(person)
    # {'name': 'Dan', 'posts_qty': 30}
    print(type(person))
    # <class 'dict'>
    info = (
        # Если не ставить запятую в конце строки (f"{person['name']} wrote ") Python автоматически объединяет две строки
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts "
    )
    return info


info = get_posts_info(name='Dan', posts_qty=30)
print(info)
# Dan wrote 30 posts

# _________________________________________________________

# Можно ли в функцию передавать позиционные аргументы
# !!!  Позиционный аргумент это который пишется (30), вместо (posts_qty=30) | ('Dan') - позиционный аргумент, а (name='Dan')  !!!
# !!!  Именованые аргументы это (posts_qty=30, name='Dan')  !!!
# _________________________________________________________


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(posts_qty=30, name='Dan')
print(info)
# Dan wrote 30 posts
# ___________________________________________


def get_posts_info(**person):
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info


info = get_posts_info(posts_qty=30, name='Dan')
print(info)
# Dan wrote 30 posts
# _______________________________________________________________________________

# Задача №1


def merge_list_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))


res_one = merge_list_to_dict(list_one=['a', 'b', 'c'], list_two=[10, True, []])
print(res_one)
# {'a': 10, 'b': True, 'c': []}

res_two = merge_list_to_dict(['abc'], list_two=[10, True, []])
print(res_two)
# {'abc': 10}

# # Error - SyntaxError: positional argument follows keyword argument
# res_two = merge_list_to_dict(list_one=['abc'], [10, True, []])
# print(res_two)


# res_two = merge_list_to_dict(list_one=['abc'], [10, True, []]) Такой поряд не допустимый
# res = merge_list_to_dict(['abc'], list_two=[10, True, []]) Допустимый только такой, позиционные аргументы, а потом ключевые аргументы
# После ключевых значений нельзя ставить позиционные значения (не всегда, если пайтон не понимает куда аргументы ставить в функции).


# Задача №2

def update_car_info(**car):
    car['is_available'] = True

    return car


print(update_car_info())
# {'is_available': True}

print(update_car_info(brand='ducatti', price=100.000))
# {'brand': 'ducatti', 'price': 100.0, 'is_available': True}
