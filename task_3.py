# Создайте любым способом множество из десяти вещей, которые вы
# бы взяли на необитаемый остров. Спросите у кого-то из ваших
# близких, какие вещи они взяли бы туда. Выведите на экран
# множество вещей:


my_items = {"Огниво", "Охотничий нож", "Фильтр для воды", "Палатка",
         "Фонарь", "Компас", "Аптечка", "Рыболовные снасти", "Запас спичек"}

friend_items = {"Фонарь", "Топор", "Аптечка", "Рыболовные снасти",
                "Огниво", "Фильтр для воды", "Охотничий нож", "Топор"}


"""которое взяли только вы;"""
print(f"Вещи которое взяли только вы; {my_items.difference(friend_items)}")
print()


"""которое возьмет ваш близкий человек;"""
print(f"Вещи которое возьмет только ваш близкий человек; {friend_items.difference(my_items)}")
print()


"""вещи которые есть и у вас и у вашего близкого человека."""
print(f"Вещи которые есть и у вас и у вашего близкого человека: {my_items.intersection(friend_items)}")
print()


print(f"Вы все вместе: {my_items.union(friend_items)}")