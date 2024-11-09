genres = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

 #узнайте длину обоих кортежей (это количество элементов в них);
print(f"количество элементов в genres: {len(genres)}")
print(f"количество элементов в numbers: {len(numbers)}")
print("*" * 100)


# найдите максимальный и минимальный элемент;
max_element_genres = max(genres)
max_element_numbers = max(numbers)
min_element_genres = min(genres)
min_element_numbers = min(numbers)

print(f"максимальный элемент в genres: {max_element_genres}")
print(f"максимальный элемент в numbers: {max_element_numbers}")
print(f"минимальный элемент в genres: {min_element_genres}")
print(f"минимальный элемент в numbers: {min_element_numbers}")
print("✔" * 100)


# просуммируйте элементы если это возможно;
print(sum(numbers))
print()


# отсортируйте элементы по возрастанию и убыванию в
# результате сортировки и последующих операций необходимо
# получить кортеж.
print(f"Сортировка элементов genres по возрастанию: {tuple(sorted(genres))}")
print(f"Сортировка элементов genres по убыванию: {tuple(sorted(genres, reverse=True))}")
print()
print(f"Сортировка элементов numbers по возрастанию: {tuple(sorted(numbers))}")
print(f"Сортировка элементов numbers по убыванию: {tuple(sorted(numbers, reverse=True))}")