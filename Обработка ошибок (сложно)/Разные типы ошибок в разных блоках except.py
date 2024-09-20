try:
    print(10 / 0)
    # TypeError: unsupported operand type(s) for /: 'str' and 'int'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('Continue...')
