try:
    print(10 / 5)  # 2.0
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")
    # There was no error
finally:
    print('Continue...')
