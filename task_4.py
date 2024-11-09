cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

"""преобразовать данный список в множество;"""
cinema_genres_set = set(cinema_genres)


"""добавить 2 жанра на ваш выбор (то что вы захотите);"""
cinema_genres_set.add("Боевик")
cinema_genres_set.add("Фэнтези")

"""удалить какой-то из жанров по вашему выбору;"""
cinema_genres_set.discard("Боевик")

"""удалить некий случайный жанр;"""
cinema_genres_set.pop()


"""преобразовать множество обратно в список."""
into_cinema_genres = list(cinema_genres_set)

print(into_cinema_genres)