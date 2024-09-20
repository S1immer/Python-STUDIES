def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов не целое число"

    if a >= b:
        return f"{a} больше или равно {b}"

    return f"{a} меньше {b}"


print(nums_info(True, 10))
# Один из аргументов не целое число
print(nums_info(10, 2))
# 10 больше или равно 2
print(nums_info(4, 15))
# 4 меньше 15
