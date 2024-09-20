user_data = ['Daniil', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))
# Daniil has 23 comments


# Можно другими способами
# __________________________________
print(user_info(user_data[0], user_data[1]))
# Daniil has 23 comments

print(user_info(name=user_data[0], comments_qty=user_data[1]))
# Daniil has 23 comments
# __________________________________


# __________________________________
# Задача

def process_image(image_id, image_title):
    return f"Image '{image_title}' has id {image_id}"


images = [
    {'image_id': 1, 'image_title': 'Sunset'},
    {'image_id': 2, 'image_title': 'Mountains'},
    {'image_id': 3, 'image_title': 'Beach'}
]

for image in images:
    print(process_image(**image))
    # Image 'Sunset' has id 1
    # Image 'Mountains' has id 2
    # Image 'Beach' has id 3
