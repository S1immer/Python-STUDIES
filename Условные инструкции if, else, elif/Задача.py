# def route_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Distance to youre destination is <distantion>"


# info = {'wheater': 'rain'}
# info_two = {'distance': 100}
# print(route_info(10, 10))


# def route_info(a):
#     if not isinstance(info, dict):
#         return "Расстояние до пункта назначения составляет <расстояние>"

#     if 'расстояние' in info and isinstance(info['расстояние'], int):
#         return f"Расстояние до пункта назначения составляет {info['расстояние']}"
#     else:
#         return "Информация о расстоянии недоступна"


# info = {'погода': 'дождь',
#         'расстояние': 100
#         }
# print(route_info(info))

# # 1)создайте функцию route_info, в которой будет передаваться словарь
# # 2)если в словаре есть ключ distance и его значение - целое число, верните строку "Distance to your destination is <distance>"
# # 3)иначе, если в словаре есть ключи speed и time, верните строку "Distance to your destination is <speed * time>"
# # __________________________


# ЗАДАЧА

def route_info(info):
    if ('distance' in info) and (isinstance(info['distance'], int)):
        return f"Distance to your destination is {info['distance']}"
    # elif 'speed' in info and 'time' in info and isinstance(info['speed'], int) and isinstance(info['time'], int):
    elif ('speed' and 'time' in info) and (isinstance(info['speed'], int) and (['time'], int)):
        return f"Distance to your destination is {info['speed'] * info['time']}"
    else:
        return "No distance info is available"


info = {'weather': 'rain',
        'distance': 500,
        'speed': 50.1,
        'time': 2,
        }
print(route_info(info))
# Distance to your destination is 500

info = {'weather': 'rain',
        'distance': 500.1,
        'speed': 50,
        'time': 2,
        }
print(route_info(info))
# Distance to your destination is 100

info = {'weather': 'rain',
        'distance': 500.1,
        'speed': 50.1,
        'time': 2,
        }
print(route_info(info))
# No distance info is available

# _________________________________________________________

# Есть немного упрощенный вариант для этой задачи


def route_info(info):
    if ('distance' in info) and (isinstance(info['distance'], int)):
        return f"Distance to your destination is {info['distance']}"

    if ('speed' in info) and ('time' in info) and (isinstance(info['speed'], int) and (isinstance(info['time'], int))):
        return f"Distance to your destination is {info['speed'] * info['time']}"

    return "No distance info is available"


print(route_info(
    {'weather': 'rain', 'distance': 500, 'speed': 50, 'time': 2}))
# Distance to your destination is 500

print(route_info({'weather': 'rain', 'speed': 50, 'time': 2}))
# Distance to your destination is 100

print(route_info({'weather': 'rain'}))
# No distance info is available
