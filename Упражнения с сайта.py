def double_integer(i):
    return i*2


num = 3
print(double_integer(num))

# ___________________________


def count_sheeps():
    sheeps = [True, False, False, False, True, True, True, True]
    count = 0
    for s in sheeps:
        if s:
            count += 1
    return count


print(count_sheeps())


def simple_multiplication(number):

    num_two = number % 2
    if isinstance(num_two, int):
        return number * 8
    else:
        return number * 9


print(simple_multiplication(7))


def simple_multiplication(number):
    return number * 9 if number % 2 else number * 8

# ______________________________________________


def simple_multiplication(number):

    num_two = number % 2 == 0
    if isinstance(num_two, int):
        return number * 8
    else:
        return number * 9


print(simple_multiplication(2))
# Не правильно

# ______________________________________________


def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9


number = 1
print(simple_multiplication(number))
# Если число четное, то функция умножает это четное число на 8
# А если число не четное, функция умножает его на 9


# _________________________________________________

def reverse_seq(n):
    if n > 0:
        return (list(range(n, 0, -1)))


# ______________________________________________________


def smash(words):
    words = ('Hello', 'My', 'Frends')
    return " ".join(words)


print(smash(words=('Hello', 'My', 'Frends')))
# Hello My Frends
# _________________________________________________________________________________Вывод в print


def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result


# Пример использования
numbers = [1, 2, 3, 4]
result = grow(numbers)
print(result)
# Вывод: 24

# ____________________________________________________________________


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


x = 2
n = 5

print(count_by(x, n))
# [2, 4, 6, 8, 10]
# _________________________________________


def f(x, y):
    return x + y, x - y,


sum, raznost = f(5, 2)

print(sum, raznost)
# 7 3
# ______________________________________________________


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


j = 1
o = 10
print(count_by(j, o))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ___________________________________________________________


def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False


b = 30
f = 5
print(check_for_factor(b, f))
# True или False, в зависимости от
# _______________________________________________________________


def remove_exclamation_marks(s):
    # Тут в () написано, что текст сначала был с !, после принения .replace, текст на выходе ставится без !.
    return s.replace('!', '')


text = ('Hello!!! My frends!')

print(remove_exclamation_marks(text))

# Эта функция убирает все восклицательные знаки из заданного текста
# Так же же можно убирать другие знаки, не обязательно (!).
# __________________________________________________________________________


def string(name):

    result = '-'.join(name)
    return result


print(string('Daniil'))
# Вывод: D-a-n-i-i-l

my_string = 'Hello'
result = '-'.join(my_string)
print(result)  # Вывод: H-e-l-l-o
# Вывод: H-e-l-l-o

# ____________________________________________________________


def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


la = 30
co = 20
ch = 10

print(goals(la, co, ch))
