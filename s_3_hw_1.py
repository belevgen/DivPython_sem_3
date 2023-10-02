# 1. Решить задачи, которые не успели решить на семинаре.
# Задание №7
# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

# Без использования метода 'count'

input_string = input("Введите строку текста: ")
letter_counts = {}

for letter in input_string:
    if letter not in letter_counts:
        letter_counts[letter] = 1
    else:
        letter_counts[letter] += 1

for letter in sorted(letter_counts.keys()):
    print(f"'{letter}': {letter_counts[letter]}")

# # С использованием метода 'count'

# input_string = input("Введите строку текста: ")
# letter_counts = {}
#
# for letter in input_string:
#     if letter not in letter_counts:
#         letter_counts[letter] = 1
#     else:
#         letter_counts[letter] += 1
#
# for letter, count in letter_counts.items():
#     print(f"'{letter}': {count}")
