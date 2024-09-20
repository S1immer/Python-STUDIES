# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
#     # division by zero

# # ___________________________________

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(type(e))
    # <class 'ZeroDivisionError'>
    print(dir(e))
    print(e)
    # division by zero
