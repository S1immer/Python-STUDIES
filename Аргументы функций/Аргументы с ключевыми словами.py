# Позиционные аргументы - ('Dan', 30) но тут нужно следить за последовательностью  заданных аргументов
# Ключевые аргументы - (name='Dan', posts_qty=30) такой код более читабельный

# posts_qty - колличество постов


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(name='Dan', posts_qty=30)
print(info)
# Dan wrote 30 posts - Дан написал 30 постов

# _______________________________________________


def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info


info = get_posts_info(posts_qty=30, name='Dan')
# Менять местами ключевые аргументы можно
# Если я уберу ключи и напишу просто аргументы info = get_posts_info(30, 'Dan'),
# тогда аргументы встанут в псоледовательность заданной функции (name, posts_qty)
# Результат безключевых аргументов выйдет (30 wrote Dan posts - 30 написал Дан постов)
print(info)
# Dan wrote 30 posts - Дан написал 30 постов
