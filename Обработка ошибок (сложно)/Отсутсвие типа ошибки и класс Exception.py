try:
    print(10 / 0)
except Exception as e:
    print(e)
    # division by zero

# Не рекомендуется использовать, так как нет инофрмации об ошибке
try:
    print(10 / 0)
except:
    print("Some error occurred")
    # Some error occurred
