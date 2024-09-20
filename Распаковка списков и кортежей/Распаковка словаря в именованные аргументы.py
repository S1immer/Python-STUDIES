user_profile = {
    'name': 'Daniil',
    'comments_qty': 23,
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile))
# Daniil has 23 comments

print(user_info(user_profile['name'], user_profile['comments_qty']))
# Daniil has 23 comments

print(user_info(name=user_profile['name'],
      comments_qty=user_profile['comments_qty']))
# Daniil has 23 comments
