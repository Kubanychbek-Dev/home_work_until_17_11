cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
updated_cinema_genres = cinema_genres[:1] + ("Боевик",) + ("Фэнтези",) + cinema_genres[2:]

print(updated_cinema_genres)
print()
genres_string = ", ".join(updated_cinema_genres)
print(f"Обновленные жанры кино: {genres_string}")