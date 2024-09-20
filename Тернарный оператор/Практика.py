my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(
    my_img) == 2 else print("Incorrect image formatting")
# 1920x1080

# Можно другим способом сделать

my_img = ('1920', '1080', True)

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Incorrect image formatting"

print(info)
# Incorrect image formatting


# ПРИМЕР с инструкцией if/else

my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}"

if len(my_img) == 2:
    print(info)

else:
    print("Incorrect image formatting")

# ___________________________________

num = "Very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very, very long string"
print("String is long" if len(num) > 79 else "String is short")
# String is long

print(len(num))
# 112
