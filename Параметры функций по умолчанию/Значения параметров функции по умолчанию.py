from datetime import date


def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(10, 2))
# 20
print(mult_by_factor(5))
# 5

# ___________________________________________


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy


inital_post = {
    'id': 243,
    'author': 'Dan Chern',
}

post_with_weekday = create_new_post(inital_post)

print(post_with_weekday)

# ______________________________________________


def get_weekday():
    return date.today().strftime('%A')


def add_book_to_library(library, book, weekday=get_weekday()):
    library_copy = library.copy()
    library_copy['created_on_weekday'] = weekday
    library_copy['book'] = book

    return library_copy


create_new_book = {
    'name': 'gold book',
    'author': 'Dan Chern',
    'genre': 'finance'
}

library = {}
# print(add_book_to_library(create_new_book))
print(add_book_to_library(library, create_new_book))
