try:
    print(10 / 0)
except ZeroDivisionError:
    print(ZeroDivisionError)
    # <class 'ZeroDivisionError'>
    print("Error - Division by zero!")
    # Error - Division by zero!
print('Continue...')
# Continue...
